(function(a) {
    'use strict';

    a.module('Header', ['ui.bootstrap', 'vocab.auth', 'kao.input', 'vocab.nav'])
        .directive('headerBar', function() {
            return {
                restrict: 'E',
                replace: true,
                controller: function($scope, $location, UserService, userEvents, $rootScope) {
                    $scope.toLogin = function() {
                        $location.path('/login/');
                    };
                    $scope.toRegister = function() {
                        $location.path('/register/');
                    };
                    $scope.logout = UserService.logout;
                    $scope.isLoggedIn = UserService.isLoggedIn;
                    
                    UserService.withUser().success(function(user) {
                        $scope.setUser(null, user);
                    }).error(function(error) {
                       console.log(error); 
                    });
                    $scope.setUser = function(event, user) {
                        $scope.user = user;
                    };
                    $rootScope.$on('user-login', $scope.setUser);
                    $rootScope.$on('user-update', $scope.setUser);
                    $rootScope.$on('user-logout', $scope.setUser);
                },
                templateUrl: 'static/partials/directives/header.html'
            };
        })
        .directive('headerNav', function() {
            return {
                restrict: 'E',
                replace: true,
                controller: function($scope, $location, $route, headerNavService) {
                    $scope.currentPath = $location.path();
                    $scope.navSections = headerNavService;
                    $scope.$on('$routeChangeSuccess', function(event, next, current) {
                        $scope.currentPath = $location.path();
                    });
                },
                templateUrl: 'static/partials/directives/header_nav.html'
            };
        })
        .directive('languagePicker', function() {
            return {
                restrict: 'E',
                replace: true,
                controller: function($scope, LanguageEnrollmentsService) {
                    LanguageEnrollmentsService.watchCurrentEnrollment($scope, function(event, currentEnrollment) {
                        $scope.currentEnrollment = currentEnrollment;
                    });
                    LanguageEnrollmentsService.watchEnrollments($scope, function(event, enrollments) {
                        $scope.enrollments = enrollments;
                    });
                    $scope.changeCurrentEnrollment = function(index) {
                        LanguageEnrollmentsService.changeCurrentEnrollment(index);
                    };
                },
                templateUrl: 'static/partials/directives/language_picker.html'
            };
        });
})(angular);