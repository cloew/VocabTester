(function(a) {
    "use strict";
    a.module('kao.auth', [])
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
            $scope.register = function() {
                userService.register($scope, function() {
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
        .controller('ChooseEnrollmentController', function ($scope, $location, CrudApiService, userService, LanguageEnrollmentsService, navService) {
            var crudApi = CrudApiService.getApiFor('Language');
            $scope.languages = [];
            userService.getUser(function(user) {
                crudApi.getAll().success(function(data) {
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
        .factory('LanguageEnrollmentsService', function($http, $q) {
            return {
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
                withCurrentEnrollment: function(callback) {
                    var findCurrentEnrollment = function(enrollments) {
                        a.forEach(enrollments, function(enrollment) {
                            if (enrollment.default) {
                                callback(enrollment);
                                return
                            }
                        });
                    };
                    if (this.enrollments === undefined) {
                        this.loadEnrollments(findCurrentEnrollment);
                    } else {
                        findCurrentEnrollment(this.enrollments);
                    }
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
                }
            };
        })
        .factory('userService', function($http, $window, $route) {
            var user = undefined;
            var userWatch = [];
            var responseHandler = function(promise, successCallback, errorCallback) {
                promise.success(function(data) {
                    if (data.error) {
                        errorCallback(data.error);
                    } else {
                        user = data.user;
                        $window.sessionStorage.token = data.token;
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
                register: function (params, successCallback, errorCallback) {
                    responseHandler($http.post('/api/users', {'email':params.email, 'password':params.password, 'givenName':params.firstName, 'lastName':params.lastName}), successCallback, errorCallback);
                },
                update: function (user, successCallback, errorCallback) {
                    responseHandler($http.put('/api/users/current', user), successCallback, errorCallback);
                },
                logout: function () {
                    delete $window.sessionStorage.token;
                    user = undefined;
                    $route.reload();
                },
                isLoggedIn: function () {
                    return $window.sessionStorage.token !== undefined;
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
        .factory('authInterceptor', function ($rootScope, $q, $window, $location) {
            return {
                request: function (config) {
                    config.headers = config.headers || {};
                    if ($window.sessionStorage.token) {
                        config.headers.Authorization = 'Bearer ' + $window.sessionStorage.token;
                    }
                    return config;
                },
                responseError: function (rejection) {
                    if (rejection.status === 401) {
                        var returnToPath = $location.path();
                        $location.path('/login').search('returnTo', returnToPath);
                    }
                    return $q.reject(rejection);
                }
            };
        })
        .config(function ($httpProvider) {
            $httpProvider.interceptors.push('authInterceptor');
        });
})(angular);