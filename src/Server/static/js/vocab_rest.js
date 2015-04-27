(function(a) {
    'use strict';
    a.module('vocab.rest', ['kao.rest', 'VocabNav'])
        .config(['CrudApiConfigProvider', 'FrontEndCrudConfigProvider', 'navConfigProvider',
            function(CrudApiConfig, FrontEndCrudConfig, navConfig) {
                var config = navConfig.config;
                CrudApiConfig.add('/api/admin/languages', [config.adminLanguages.path, config.adminNewLanguages.path, config.adminEditLanguages.path]);
                FrontEndCrudConfig.add({'name':'Language', 'listUrl':config.adminLanguages.path, 'newUrl':config.adminNewLanguages.path, 'editUrl':config.adminNewLanguages.path});
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