'use strict';

angular.module('VocabTester', ['ngRoute', 'VocabTesterControllers', 'VocabTesterDirectives', 'Concepts', 'Symbols', 'Words', 'Quiz', 'VocabNavServices'])
	.config(['$routeProvider', 'navConfigProvider',
		function($routeProvider, navConfig) {
            var navConfig = navConfig.getConfig();
            for (var i = 0; i < navConfig.length; i++) {
                $routeProvider.when(navConfig[i].path, navConfig[i]);
            }
		$routeProvider.otherwise({
			redirectTo: '/'
		});
	}]);