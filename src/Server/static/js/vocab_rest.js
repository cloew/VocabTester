(function(a) {
    'use strict';
    a.module('vocab.rest', ['kao.rest', 'VocabNav'])
        .config(['CrudApiConfigProvider', 'navConfigProvider',
            function(CrudApiConfig, navConfig) {
                var config = navConfig.config;
                CrudApiConfig.add('/api/admin/languages', [config.adminLanguages.path, config.adminNewLanguages.path, config.adminEditLanguages.path]);
            }
        ])
        .directive('languageTable', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/language_table.html'
            }
        })
        .directive('languageForm', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/language_form.html'
            }
        });
})(angular);