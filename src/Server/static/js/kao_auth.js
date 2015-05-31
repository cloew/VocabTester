(function(a) {
    "use strict";
    a.module('kao.auth', ['kao.loading', 'kao.utils'])
        .controller('LoginController', function ($scope, $location, userService) {
            $scope.login = function() {
                userService.login($scope.email, $scope.password, function() {
                    var next = $location.search().returnTo;
                    if (!next) {
                        next = '/'
                    }
                    $location.path(next);
                    $location.search('returnTo', null);
                }, function(error) {
                    $scope.errorMessage = error.message;
                });
            };
        })
        .controller('RegisterController', function ($scope, $location, userService) {
            $scope.user = {};
            $scope.register = function() {
                userService.register($scope.user, function() {
                    $location.path('/');
                }, function(error) {
                    $scope.errorMessage = error.message;
                });
            };
        })
        .controller('ProfileController', function ($scope, $location, userService, LanguageEnrollmentsService) {
            $scope.user = {};
            LanguageEnrollmentsService.requestEnrollments(function(enrollments) {
                $scope.enrollments = enrollments;
            });
            userService.getUser(function(user) {
                a.copy(user, $scope.user);
            });
            
            $scope.update = function() {
                userService.update($scope.user, function() {
                }, function(error) {
                    $scope.errorMessage = error.message;
                });
            };
        })
        .controller('ChooseEnrollmentController', function ($scope, $location, languages, userService, LanguageEnrollmentsService, navService, LoadingTrackerService) {
            $scope.languages = [];
            var tracker = LoadingTrackerService.get('enrollments');
            userService.getUser(function(user) {
                tracker.load(languages()).success(function(data) {
                    LanguageEnrollmentsService.requestEnrollments(function(enrollments) {
                        var enrolledLanguageIds = [];
                        a.forEach(enrollments, function(enrollment, key) {
                            enrolledLanguageIds.push(enrollment.language.id);
                        });
                        a.forEach(data.records, function(language, key) {
                            if (language.id !== user.nativeLanguage.id && enrolledLanguageIds.indexOf(language.id) === -1) {
                                $scope.languages.push(language);
                            }
                        });
                    });
                }).error(function(error) {
                    console.log(error);
                });
            });
            
            $scope.enroll = function(language) {
                LanguageEnrollmentsService.create(language).then(function(data) {
                    $location.path(navService.profile.path);
                }, function(error) {
                    console.log(error);
                });
            }
        })
        .factory('LanguageEnrollmentsService', function($http, $q, $rootScope, $timeout, KaoPromise) {
            return {
                currentChangedEventType: 'current-enrollment-changed',
                loadEnrollments: function(callback) {
                    var self = this;
                    $http.get('/api/users/current/enrollments').success(function(data) {
                        self.enrollments = data.enrollments;
                        callback(self.enrollments);
                    }).error(function(error) {
                        console.log(error);
                    });
                },
                loadEnrollments: function(callback) {
                    var self = this;
                    $http.get('/api/users/current/enrollments').success(function(data) {
                        self.enrollments = data.enrollments;
                        callback(self.enrollments);
                    }).error(function(error) {
                        console.log(error);
                    });
                },
                enrollments: undefined,
                requestEnrollments: function(callback) {
                    if (this.enrollments === undefined) {
                        this.loadEnrollments(callback);
                    } else {
                        callback(this.enrollments);
                    }
                },
                withCurrentEnrollment: function() {
                    var deferred = KaoPromise();
                    var findCurrentEnrollment = function(enrollments) {
                        for (var i = 0; i < enrollments.length; i++) {
                            var enrollment = enrollments[i];
                            if (enrollment.default) {
                                deferred.resolve(enrollment);
                                return;
                            }
                        }
                        deferred.reject();
                    };
                    var self = this;
                    $timeout(function() {
                        if (self.enrollments === undefined) {
                            self.loadEnrollments(findCurrentEnrollment);
                        } else {
                            findCurrentEnrollment(self.enrollments);
                        }
                    }, 0);
                    return deferred.promise;
                },
                watchCurrentEnrollment: function(scope, callback) {
                    scope.$on(this.currentChangedEventType, callback);
                    this.withCurrentEnrollment().success(function(currentEnrollment) {
                        callback(undefined, currentEnrollment);
                    });
                },
                create: function(language, callback) {
                    var deferred = $q.defer();
                    var self = this;
                    $http.post('/api/users/current/enrollments', {language:language}).success(function(data) {
                        self.requestEnrollments(function(enrollments) {
                            enrollments.push(data.record);
                        });
                        deferred.resolve(data);
                    }).error(function(error) {
                        deferred.reject(error);
                    });
                    return deferred.promise;
                },
                changeCurrentEnrollment: function(index) {
                    var self = this;
                    this.withCurrentEnrollment().success(function(currentEnrollment) {
                        currentEnrollment.default = false;
                        self.enrollments[index].default = true;
                        $rootScope.$broadcast(self.currentChangedEventType, self.enrollments[index]);
                    });
                }
            };
        })
        .factory('userService', function($http, $window, $location, navService) {
            var user = undefined;
            var userWatch = [];
            var responseHandler = function(promise, successCallback, errorCallback) {
                promise.success(function(data) {
                    if (data.error) {
                        errorCallback(data.error);
                    } else {
                        user = data.user;
                        $window.localStorage.token = data.token;
                        successCallback();
                        for (var i = 0; i < userWatch.length; i++) {
                            userWatch[i](user);
                        }
                    }
                }).error(function(error) {
                    console.log(error);
                });
            }

            return {
                login: function (email, password, successCallback, errorCallback) {
                    responseHandler($http.post('/api/login', {'email':email, 'password':password}), successCallback, errorCallback);
                },
                register: function (user, successCallback, errorCallback) {
                    responseHandler($http.post('/api/users', user), successCallback, errorCallback);
                },
                update: function (user, successCallback, errorCallback) {
                    responseHandler($http.put('/api/users/current', user), successCallback, errorCallback);
                },
                logout: function () {
                    delete $window.localStorage.token;
                    user = undefined;
                    $location.path(navService.login.path);
                },
                isLoggedIn: function () {
                    return $window.localStorage.token !== undefined;
                },
                getUser: function (callback) {
                    if (this.isLoggedIn() && (user === undefined)) {
                        $http.get('/api/users/current').success(function(data) {
                            user = data.user;
                            callback(user);
                        }).error(function(error) {
                            console.log(error);
                        });
                    } else {
                        callback(user);
                    }
                },
                watchUser: function(callback) {
                    userWatch.push(callback);
                    
                    if (this.isLoggedIn()) {
                        this.getUser(function(user) {
                            if (user !== undefined) {
                                callback(user);
                            }
                        });
                    }
                }
            };
        })
        .service('AuthRejected', function ($location) {
            return {
                toLogin: function () {
                    var returnToPath = $location.path();
                    $location.path('/login').search('returnTo', returnToPath);
                }
            };
        })
        .factory('authInterceptor', function ($rootScope, $q, $window, AuthRejected) {
            return {
                request: function (config) {
                    config.headers = config.headers || {};
                    if ($window.localStorage.token) {
                        config.headers.Authorization = 'Bearer ' + $window.localStorage.token;
                    }
                    return config;
                },
                responseError: function (rejection) {
                    if (rejection.status === 401) {
                        AuthRejected.toLogin();
                    }
                    return $q.reject(rejection);
                }
            };
        })
        .service('requireAuth', function(userService, AuthRejected) {
            return function(event) {
                if (!userService.isLoggedIn()) {
                    event.preventDefault();
                    AuthRejected.toLogin();
                }
            };
        })
        .service('requireEnrollment', function($location, LanguageEnrollmentsService, navService) {
            return function(event) {
                LanguageEnrollmentsService.withCurrentEnrollment().error(function() {
                    $location.path(navService.enroll.path);
                });
            };
        })
        .config(function ($httpProvider) {
            $httpProvider.interceptors.push('authInterceptor');
        });
})(angular);