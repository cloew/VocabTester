'use strict';

angular.module('VocabTester', ['ngRoute', 'VocabTesterControllers', 'VocabTesterDirectives', 'VocabTesterServices'])
	.config(['$routeProvider', 'vocabNavProvider',
		function($routeProvider, vocabNav) {
            var navConfig = vocabNav.getConfig();
            for (var i = 0; i < navConfig.length; i++) {
                $routeProvider.when(navConfig[i].path, navConfig[i]);
            }
		$routeProvider.otherwise({
			redirectTo: '/'
		});
	}]);