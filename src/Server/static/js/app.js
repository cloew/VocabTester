'use strict';

angular.module('VocabTester', ['ngRoute', 'VocabTesterControllers', 'VocabTesterDirectives'])
	.config(['$routeProvider',
		function($routeProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/index.html',
			controller: 'IndexController'
		})
		.when('/symbollists', {
			templateUrl: 'static/partials/symbol_lists.html',
		})
		.when('/login', {
			templateUrl: 'static/partials/login.html',
			controller: 'LoginController'
		})
		.when('/register', {
			templateUrl: 'static/partials/register.html',
			controller: 'RegisterController'
		})
		.when('/symbollist/:listId/quiz', {
			templateUrl: 'static/partials/quiz.html',
			controller: 'QuizController'
		})
		.when('/wordlist/:listId/quiz', {
			templateUrl: 'static/partials/quiz.html',
			controller: 'QuizController'
		})
		.otherwise({
			redirectTo: '/'
		});
	}]);