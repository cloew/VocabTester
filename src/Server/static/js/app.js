'use strict';

angular.module('VocabTester', ['ngRoute', 'VocabTesterControllers', 'VocabTesterDirectives', 'VocabTesterServices', 'VocabNavServices', 'Quiz'])
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