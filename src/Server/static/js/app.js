'use strict';

angular.module('VocabTester', ['ui.bootstrap', 'ngRoute', 'Header', 'Concepts', 'Symbols', 'Words', 'Quiz', 'VocabNavServices', 'kao.auth'])
	.config(['$routeProvider', 'navConfigProvider',
		function($routeProvider, navConfig) {
            var navConfig = navConfig.getConfig();
            for (var i = 0; i < navConfig.length; i++) {
                $routeProvider.when(navConfig[i].path, navConfig[i]);
            }
		$routeProvider.otherwise({
			redirectTo: '/'
		});
	}])
    .controller('IndexController', function ($scope, userService) {
        $scope.isLoggedIn = userService.isLoggedIn;
    })
    .directive('info', function() {
        return {
            restrict: 'E',
            replace: true,
            controller: function($scope, $location, userService) {
                $scope.toRegister = function() {
                    $location.path('/register/');
                };
            },
            templateUrl: 'static/partials/directives/info.html'
            }
        });