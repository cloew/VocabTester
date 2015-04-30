(function(a) {
    'use strict';
    a.module('vocab.rest', ['kao.rest', 'VocabNav'])
        .config(['CrudApiConfigProvider', 'FrontEndCrudConfigProvider', 'CrudParamFromRouteConfigProvider', 'navConfigProvider',
            function(CrudApiConfig, FrontEndCrudConfig, CrudParamFromRouteConfig, navConfig) {
                var config = navConfig.config;
                CrudParamFromRouteConfig.register('conceptId', [{path:config.adminEditConcepts.path, param: 'id'},
                                                                {path:config.adminNewConceptWords.path, param: 'conceptId'},
                                                                {path:config.adminEditConceptWords.path, param: 'conceptId'}]);
                
                CrudApiConfig.add('/api/admin/languages', 'Language');
                FrontEndCrudConfig.add({'name':'Language', 'listUrl':config.adminLanguages.path, 'newUrl':config.adminNewLanguages.path, 'editUrl':config.adminEditLanguages.path,
                                        'formDirective':'language-form', 'tableDirective':'language-table'});
                CrudApiConfig.add('/api/admin/concepts', 'Concept');
                FrontEndCrudConfig.add({'name':'Concept', 'listUrl':config.adminConcepts.path, 'newUrl':config.adminNewConcepts.path, 'editUrl':config.adminEditConcepts.path,
                                        'formDirective':'admin-concept-form', 'tableDirective':'admin-concept-table'});
                CrudApiConfig.add('/api/admin/concepts/:conceptId/words', 'Word', [{param: 'conceptId', provider: CrudParamFromRouteConfig.forParam('conceptId')}]);
                FrontEndCrudConfig.add({name:'Word', listUrl:config.adminEditConcepts.path, newUrl:config.adminNewConceptWords.path, editUrl:config.adminEditConceptWords.path,
                                        formDirective:'admin-concept-form-form', tableDirective:'admin-concept-form-table',
                                        nested:[{param: 'conceptId', provider: CrudParamFromRouteConfig.forParam('conceptId'), list:'id'}],
                                        primaryPaths:[config.adminNewConceptWords.path, config.adminEditConceptWords.path]});
                CrudApiConfig.add('/api/admin/concepts/:conceptId/symbols', 'Symbol', [{param: 'conceptId', provider: CrudParamFromRouteConfig.forParam('conceptId')}]);
                FrontEndCrudConfig.add({name:'Symbol', listUrl:config.adminEditConcepts.path, newUrl:config.adminNewConceptSymbols.path, editUrl:config.adminEditConceptSymbols.path,
                                        formDirective:'admin-concept-form-form', tableDirective:'admin-concept-form-table',
                                        nested:[{param: 'conceptId', provider: CrudParamFromRouteConfig.forParam('conceptId'), list:'id'}],
                                        primaryPaths:[config.adminNewConceptSymbols.path, config.adminEditConceptSymbols.path]});
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
        })
        .directive('adminConceptTable', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/concept_table.html'
            }
        })
        .directive('adminConceptForm', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/concept_form.html'
            }
        })
        .directive('adminConceptFormTable', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/concept_form_table.html'
            }
        })
        .directive('adminConceptFormForm', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/concept_form_form.html'
            }
        });
})(angular);