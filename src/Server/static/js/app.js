'use strict';

angular.module('VocabTester', ['ui.bootstrap', 'ngRoute', 'Header', 'Concepts', 'Words', 'Quiz', 'kao.auth', 'kao.crud.api', 'vocab.nav', 'vocab.rest'])
	.config(['$routeProvider', 'NavConfigProvider',
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
            templateUrl: 'static/partials/directives/info.html'
            }
        });