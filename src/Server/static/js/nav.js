(function(a) {
    'use strict';

    var services = angular.module('VocabNav', ['ngRoute'])
        .provider('navConfig', function() {
            this.config = {};
            this.routes = []
            this.add = function(config) {
                this.config[config.name] = config;
                this.routes.push(config);
            };
            this.add({name: 'wordLists', path:'/', templateUrl:'static/partials/index.html', controller:'IndexController'});
            this.add({name: 'login', path:'/login', templateUrl:'static/partials/login.html', controller:'LoginController'});
            this.add({name: 'register', path:'/register', templateUrl:'static/partials/register.html', controller:'RegisterController'});
            this.add({name: 'profile', path:'/profile', templateUrl:'static/partials/profile.html', controller:'ProfileController', onLoad: ['requireAuth']});
            this.add({name: 'enroll', path:'/enroll', templateUrl:'static/partials/enroll.html', controller:'ChooseEnrollmentController', onLoad: ['requireAuth']});
            this.add({name: 'words', path:'/words', templateUrl:'static/partials/learned_concepts.html', controller:'LearnedFormsController', onLoad: ['requireAuth']});
            this.add({name: 'symbols', path:'/symbols', templateUrl:'static/partials/learned_concepts.html', controller:'LearnedFormsController', onLoad: ['requireAuth']});
            this.add({name: 'symbolLists', path:'/symbollists', template:'<form-lists></form-lists>', onLoad: ['requireAuth']});
            this.add({name: 'search', path:'/search', templateUrl:'static/partials/search.html', controller:'SearchController', onLoad: ['requireAuth']});
            this.add({name: 'adminLanguages', path:'/admin/languages', templateUrl:'static/partials/admin/list_records.html', onLoad: ['requireAuth']});
            this.add({name: 'adminNewLanguages', path:'/admin/languages/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminEditLanguages', path:'/admin/languages/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminConcepts', path:'/admin/concepts', templateUrl:'static/partials/admin/list_records.html', onLoad: ['requireAuth']});
            this.add({name: 'adminNewConcepts', path:'/admin/concepts/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminEditConcepts', path:'/admin/concepts/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminNewConceptWords', path:'/admin/concepts/:conceptId/words/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminEditConceptWords', path:'/admin/concepts/:conceptId/words/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminNewConceptSymbols', path:'/admin/concepts/:conceptId/symbols/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            this.add({name: 'adminEditConceptSymbols', path:'/admin/concepts/:conceptId/symbols/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            this.add({name: 'randomSymbolQuiz', path:'/symbollist/random/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth'], returnTo:this.config.symbols.path});
            this.add({name: 'symbolListQuiz', path:'/symbollist/:listId/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth'], returnTo:this.config.symbolLists.path});
            this.add({name: 'randomWordQuiz', path:'/wordlist/random/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth'], returnTo:this.config.words.path});
            this.add({name: 'wordListQuiz', path:'/wordlist/:listId/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth'], returnTo:this.config.wordLists.path});
            
            this.$get = function() {
                return this;
            };
        })
        .factory('navService', function($location, $route, navConfig) {
            var theService = {
                getNavFor: function(path) {
                    for (var i = 0; i < navConfig.routes.length; i++) {
                        if (navConfig.routes[i].path === path) {
                            return navConfig.routes[i];
                        }
                    }
                    return undefined;
                },
                getCurrentNav: function() {
                    return getNavFor($route.current.$$route.path);
                },
                getReturnTo: function() {
                    var currentConfig = this.getCurrentNav();
                    if (currentConfig !== undefined) {
                        return currentConfig.returnTo;
                    }
                    return undefined;
                },
                getApiUrl: function() {
                    var currentConfig = this.getCurrentNav();
                    if (currentConfig !== undefined) {
                        if (currentConfig.apiUrl) {
                            return '/api' + currentConfig.apiUrl;
                        } else {
                            return '/api' + $location.path();
                        }
                    }
                    return undefined;
                }};
            for (var i = 0; i < navConfig.routes.length; i++) {
                theService[navConfig.routes[i].name] = navConfig.routes[i];
            }
            
            return theService;
        })
        .factory('headerNavService', function(navService) {
            return [{name: 'Words', path: navService.words.path},
                    {name: 'Word Lists', path: navService.wordLists.path},
                    {name: 'Symbols', path: navService.symbols.path},
                    {name: 'Symbol Lists', path: navService.symbolLists.path},
                    {name: 'Search', path: navService.search.path}];
        })
        .run(function($injector, $rootScope, navService) {
            $rootScope.$on('$routeChangeStart', function(event, next, current) {
                var nav = navService.getNavFor(next.$$route.path);
                a.forEach(nav.onLoad, function(serviceName) {
                    if (!event.defaultPrevented) {
                        $injector.get(serviceName)(event);
                    }
                });
            });
        });
})(angular);