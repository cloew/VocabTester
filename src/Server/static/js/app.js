'use strict';

angular.module('VocabTester', ['ngRoute', 'VocabTesterControllers', 'VocabTesterDirectives'])
	.config(['$routeProvider',
		function($routeProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/word_lists.html',
			controller: 'WordListsController'
		})
		.when('/login', {
			templateUrl: 'static/partials/login.html',
			controller: 'LoginController'
		})
		.when('/wordlist/:wordlistId/quiz', {
			templateUrl: 'static/partials/quiz.html',
			controller: 'QuizController'
		})
		.otherwise({
			redirectTo: '/'
		})
		;
	}]);