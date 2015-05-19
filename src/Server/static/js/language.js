(function(a) {
    "use strict";
    a.module('Language', ['kao.auth'])
        .factory('Language', function($http, $location) {
            function Langauge(language) {
                this.language = language;
                this.baseApiUrl = '/api/languages/'+this.language.id;
            };
            Langauge.prototype.getSymbols = function() {
                return $http.get(this.baseApiUrl+'/symbols');
            };
            Langauge.prototype.getSymbolLists = function() {
                return $http.get(this.baseApiUrl+'/symbollists');
            };
            Langauge.prototype.getWords = function() {
                return $http.get(this.baseApiUrl+'/words');
            };
            Langauge.prototype.getWordLists = function() {
                return $http.get(this.baseApiUrl+'/wordlists');
            };
            Langauge.prototype.getQuiz = function() {
                return $http.get(this.baseApiUrl+$location.path());
            };
            return Langauge;
        })
        .service('LanguageService', function($rootScope, Language, LanguageEnrollmentsService) {
            var currentLanguage = undefined;
            var service = {
                currentLanguageChangedEventType: 'current-language-changed',
                withCurrentLanguage: function(callback) {
                    if (currentLanguage !== undefined) {
                        callback(currentLanguage);
                    } else {
                        LanguageEnrollmentsService.withCurrentEnrollment(function(enrollment) {
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
        });
})(angular);