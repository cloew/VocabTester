(function(a) {
    "use strict";
    a.module('vocab.auth.controllers', ['kao.loading', 'kao.utils', 'kao.nav'])
        .controller('LoginController', function ($scope, $location, UserService, NavService) {
            $scope.login = function() {
                UserService.login({'email':$scope.email, 'password':$scope.password}).success(function(user) {
                    var next = $location.search().returnTo;
                    if (!next) {
                        next = NavService.wordLists.path;
                    }
                    $location.path(next);
                    $location.search('returnTo', null);
                }).error(function(error) {
                    $scope.errorMessage = error.message;
                });
            };
        })
        .controller('RegisterController', function ($scope, UserService, NavService) {
            $scope.user = {};
            $scope.register = function() {
                UserService.register($scope.user).success(function(user) {
                    NavService.enroll.goTo();
                }).error(function(error) {
                    $scope.errorMessage = error.message;
                });
            };
        })
        .controller('ProfileController', function ($scope, UserService, LanguageEnrollmentsService) {
            $scope.user = {};
            LanguageEnrollmentsService.requestEnrollments(function(enrollments) {
                $scope.enrollments = enrollments;
            });
            UserService.withUser().success(function(user) {
                a.copy(user, $scope.user);
            }).error(function(error) {
                console.log(error);
            });
            
            $scope.update = function() {
                UserService.update($scope.user).success(function(user) {
                }).error(function(error) {
                    $scope.errorMessage = error.message;
                });
            };
        })
        .controller('ChooseEnrollmentController', function ($scope, languages, UserService, LanguageEnrollmentsService, NavService, LoadingTracker) {
            $scope.languages = [];
            $scope.tracker = new LoadingTracker();
            UserService.withUser().success(function(user) {
                $scope.tracker.load(languages()).success(function(data) {
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
            }).error(function(error) {
                console.log(error);
            });
            
            $scope.enroll = function(language) {
                LanguageEnrollmentsService.create(language).then(function(data) {
                    NavService.profile.goTo();
                }, function(error) {
                    console.log(error);
                });
            }
        })
        .factory('LanguageEnrollmentsService', function($http, $q, $rootScope, $timeout, KaoDefer) {
            var service = {
                currentChangedEventType: 'current-enrollment-changed',
                enrollmentsChangedEventType: 'enrollments-changed',
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
                watchEnrollments: function(scope, callback) {
                    scope.$on(this.enrollmentsChangedEventType, callback);
                    this.requestEnrollments(function(enrollments) {
                        callback(undefined, enrollments);
                    });
                },
                withCurrentEnrollment: function() {
                    var deferred = KaoDefer();
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
                            if (enrollments.length === 0) {
                                data.record.default = true;
                                $rootScope.$broadcast(self.currentChangedEventType, data.record);
                            }
                            enrollments.push(data.record);
                            $rootScope.$broadcast(self.enrollmentsChangedEventType, enrollments);
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
            $rootScope.$on('user-logout', function() {
                service.enrollments = undefined;
            });
            return service;
        })
        .service('requireEnrollment', function($location, LanguageEnrollmentsService, NavService) {
            return function(event) {
                LanguageEnrollmentsService.withCurrentEnrollment().error(function() {
                    $location.path(NavService.enroll.path);
                });
            };
        });
})(angular);