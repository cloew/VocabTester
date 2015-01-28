'use strict';

var services = angular.module('VocabNavServices', ['ngRoute']);

services.provider('navConfig', function() {
    var wordLists = {name: 'wordLists', path:'/', templateUrl:'static/partials/index.html', controller:'IndexController'}
    var login = {name: 'login', path:'/login', templateUrl:'static/partials/login.html', controller:'LoginController'};
    var register = {name: 'register', path:'/register', templateUrl:'static/partials/register.html', controller:'RegisterController'};
    var words = {name: 'words', path:'/words', templateUrl:'static/partials/learned_words.html', controller:'LearnedFormsController'};
    var symbols = {name: 'symbols', path:'/symbols', templateUrl:'static/partials/learned_symbols.html', controller:'LearnedFormsController'};
    var symbolLists = {name: 'symbolLists', path:'/symbollists', templateUrl:'static/partials/symbol_lists.html'};
    var randomSymbolQuiz = {name: 'randomSymbolQuiz', path:'/symbollist/random/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', returnTo:symbols.path};
    var symbolListQuiz = {name: 'symbolListQuiz', path:'/symbollist/:listId/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', returnTo:symbolLists.path};
    var randomWordQuiz = {name: 'randomWordQuiz', path:'/wordlist/random/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', returnTo:words.path};
    var wordListQuiz = {name: 'wordListQuiz', path:'/wordlist/:listId/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', returnTo:wordLists.path};
    var nav = [wordLists, login, register, words, symbols, symbolLists, randomSymbolQuiz, symbolListQuiz, randomWordQuiz, wordListQuiz];
    this.getConfig = function() {
        return nav;
    };
    this.$get = function() {
        return nav;
    };
}).factory('navService', function($location, $route, navConfig) {
    var theService = {
        getReturnTo: function() {
            for (var i = 0; i < navConfig.length; i++) {
                if (navConfig[i].path === $route.current.$$route.path) {
                    return navConfig[i].returnTo;
                }
            }
            return undefined;
        }};
    for (var i = 0; i < navConfig.length; i++) {
        theService[navConfig[i].name] = navConfig[i];
    }
    
    return theService;
}).factory('headerNavService', function(navService) {
    return [{name: 'Words', path: navService.words.path},
            {name: 'Word Lists', path: navService.wordLists.path},
            {name: 'Symbols', path: navService.symbols.path},
            {name: 'Symbol Lists', path: navService.symbolLists.path}];
});
