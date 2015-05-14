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
                logout: function () {
                    delete $window.sessionStorage.token;
                    user = undefined;
                    $route.reload();
                },
                isLoggedIn: function () {
                    return $window.sessionStorage.token !== undefined
                },
                watchUser: function(callback) {
                    userWatch.push(callback);
                    if (this.isLoggedIn()) {
                        if (user === undefined) {
                            $http.get('/api/users/current').success(function(data) {
                                user = data.user;
                                callback(user);
                            }).error(function(error) {
                                console.log(error);
                            });
                        } else  {
                            callback(user);
                        }
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