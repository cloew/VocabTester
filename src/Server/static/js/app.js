'use strict';

angular.module('VocabTester', ['ui.bootstrap', 'ngRoute', 'Header', 'Concepts', 'Symbols', 'Words', 'Quiz', 'VocabNav', 'kao.auth', 'kao.rest', 'vocab.rest'])
	.config(['$routeProvider', 'navConfigProvider',
		function($routeProvider, navConfig) {
            var routes = navConfig.routes;
            for (var i = 0; i < routes.length; i++) {
                $routeProvider.when(routes[i].path, routes[i]);
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