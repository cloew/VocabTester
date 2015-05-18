(function(a) {
    "use strict";
    a.module('Language', ['kao.auth'])
        .factory('Language', function($http) {
            function Langauge(language) {
                this.language = language;
                this.baseApiUrl = '/api/languages/'+this.language.id;
            };
            Langauge.prototype.getSymbols = function() {
                return $http.get(this.baseApiUrl+'/symbols');
            };
            Langauge.prototype.getWords = function() {
                return $http.get(this.baseApiUrl+'/words');
            };
            return Langauge;
        })
        .service('LanguageService', function(Language, LanguageEnrollmentsService) {
            return {withCurrentLanguage: function(callback) {
                LanguageEnrollmentsService.withCurrentEnrollment(function(enrollment) {
                    callback(new Language(enrollment.language));
                });
            }};
        });
})(angular);