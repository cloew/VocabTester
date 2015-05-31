(function(a) {
    "use strict";
    a.module('Language', ['kao.auth'])
        .factory('Language', function($http, $location) {
            function Language(language) {
                this.language = language;
                this.baseApiUrl = '/api/languages/'+this.language.id;
            };
            Language.prototype.getSymbols = function() {
                return $http.get(this.baseApiUrl+'/symbols');
            };
            Language.prototype.getSymbolLists = function() {
                return $http.get(this.baseApiUrl+'/symbollists');
            };
            Language.prototype.getWords = function() {
                return $http.get(this.baseApiUrl+'/words');
            };
            Language.prototype.getWordLists = function() {
                return $http.get(this.baseApiUrl+'/wordlists');
            };
            Language.prototype.getQuiz = function() {
                return $http.get(this.baseApiUrl+$location.path());
            };
            Language.prototype.search = function(data) {
                return $http.post(this.baseApiUrl+'/search', data);
            };
            return Language;
        })
        .service('LanguageService', function($rootScope, Language, LanguageEnrollmentsService) {
            var currentLanguage = undefined;
            var service = {
                currentLanguageChangedEventType: 'current-language-changed',
                withCurrentLanguage: function(callback) {
                    if (currentLanguage !== undefined) {
                        callback(currentLanguage);
                    } else {
                        LanguageEnrollmentsService.withCurrentEnrollment().success(function(enrollment) {
                            callback(new Language(enrollment.language));
                        });
                    }
                },
                watchCurrentLanguage: function(scope, callback) {
                    scope.$on(this.currentLanguageChangedEventType, callback);
                    if (currentLanguage !== undefined) {
                        callback(undefined, currentLanguage);
                    }
            }};
            LanguageEnrollmentsService.watchCurrentEnrollment($rootScope, function(event, enrollment) {
                currentLanguage = new Language(enrollment.language);
                $rootScope.$broadcast(service.currentLanguageChangedEventType, currentLanguage);
            });
            return service;
        })
        .service('languages', function($http) {
            return function() {return $http.get('/api/languages');}
        });
})(angular);