(function(a) {
    'use strict';

    var services = angular.module('vocab.nav', ['kao.nav', 'vocab.auth.controllers'])
        .config(['NavConfigProvider', function(navConfig) {
            navConfig.add({name: 'index', path:'/', templateUrl:'static/partials/index.html', controller:'IndexController'});
            navConfig.add({name: 'login', path:'/login', templateUrl:'static/partials/login.html', controller:'LoginController'});
            navConfig.add({name: 'register', path:'/register', templateUrl:'static/partials/register.html', controller:'RegisterController'});
            navConfig.add({name: 'enroll', path:'/enroll', templateUrl:'static/partials/enroll.html', controller:'ChooseEnrollmentController', onLoad: ['requireAuth']});
            navConfig.add({name: 'profile', path:'/profile', templateUrl:'static/partials/profile.html', controller:'ProfileController', onLoad: ['requireAuth', 'requireEnrollment']});
            navConfig.add({name: 'words', path:'/words', templateUrl:'static/partials/learned_concepts.html', controller:'LearnedFormsController', onLoad: ['requireAuth', 'requireEnrollment']});
            navConfig.add({name: 'wordLists', path:'/wordlists', template:'<form-lists></form-lists>', onLoad: ['requireAuth', 'requireEnrollment']});
            navConfig.add({name: 'symbols', path:'/symbols', templateUrl:'static/partials/learned_concepts.html', controller:'LearnedFormsController', onLoad: ['requireAuth', 'requireEnrollment']});
            navConfig.add({name: 'symbolLists', path:'/symbollists', template:'<form-lists></form-lists>', onLoad: ['requireAuth', 'requireEnrollment']});
            navConfig.add({name: 'search', path:'/search', templateUrl:'static/partials/search.html', controller:'SearchController', onLoad: ['requireAuth', 'requireEnrollment']});
            navConfig.add({name: 'adminUsers', path:'/admin/users', templateUrl:'static/partials/admin/list_records.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminNewUsers', path:'/admin/users/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminEditUsers', path:'/admin/users/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminLanguages', path:'/admin/languages', templateUrl:'static/partials/admin/list_records.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminNewLanguages', path:'/admin/languages/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminEditLanguages', path:'/admin/languages/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminConcepts', path:'/admin/concepts', templateUrl:'static/partials/admin/list_records.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminNewConcepts', path:'/admin/concepts/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminEditConcepts', path:'/admin/concepts/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminNewConceptWords', path:'/admin/concepts/:conceptId/words/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminEditConceptWords', path:'/admin/concepts/:conceptId/words/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminNewConceptSymbols', path:'/admin/concepts/:conceptId/symbols/new', templateUrl:'static/partials/admin/new_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'adminEditConceptSymbols', path:'/admin/concepts/:conceptId/symbols/:id', templateUrl:'static/partials/admin/edit_record.html', onLoad: ['requireAuth']});
            navConfig.add({name: 'randomSymbolQuiz', path:'/symbollist/random/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth', 'requireEnrollment'], returnTo:navConfig.config.symbols.path});
            navConfig.add({name: 'symbolListQuiz', path:'/symbollist/:listId/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth', 'requireEnrollment'], returnTo:navConfig.config.symbolLists.path});
            navConfig.add({name: 'randomWordQuiz', path:'/wordlist/random/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth', 'requireEnrollment'], returnTo:navConfig.config.words.path});
            navConfig.add({name: 'wordListQuiz', path:'/wordlist/:listId/quiz', templateUrl:'static/partials/quiz.html', controller:'QuizController', onLoad: ['requireAuth', 'requireEnrollment'], returnTo:navConfig.config.wordLists.path});
        }])
        .factory('headerNavService', function(NavService) {
            return [{name: 'Words', path: NavService.words.path},
                    {name: 'Word Lists', path: NavService.wordLists.path},
                    {name: 'Symbols', path: NavService.symbols.path},
                    {name: 'Symbol Lists', path: NavService.symbolLists.path},
                    {name: 'Search', path: NavService.search.path},
                    {name: 'Admin', path: NavService.adminConcepts.path, if: "userService.isLoggedIn()"}];
        });
})(angular);