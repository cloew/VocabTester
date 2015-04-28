(function(a) {
    'use strict';
    a.module('vocab.rest', ['kao.rest', 'VocabNav'])
        .config(['CrudApiConfigProvider', 'FrontEndCrudConfigProvider', 'navConfigProvider',
            function(CrudApiConfig, FrontEndCrudConfig, navConfig) {
                var config = navConfig.config;
                CrudApiConfig.add('/api/admin/languages', 'Language');
                FrontEndCrudConfig.add({'name':'Language', 'listUrl':config.adminLanguages.path, 'newUrl':config.adminNewLanguages.path, 'editUrl':config.adminEditLanguages.path,
                                        'formDirective':'language-form', 'tableDirective':'language-table'});
                CrudApiConfig.add('/api/admin/concepts', 'Concept');
                FrontEndCrudConfig.add({'name':'Concept', 'listUrl':config.adminConcepts.path, 'newUrl':config.adminNewConcepts.path, 'editUrl':config.adminEditConcepts.path,
                                        'formDirective':'admin-concept-form', 'tableDirective':'admin-concept-table'});
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
        .controller('WordsTableController', function ($scope, $routeParams, $http, $route) {
            $scope.records = [];
            
            $scope.getRecords = function() {
                $http.get('/api/admin/concepts/'+$routeParams.id+'/words').success(function(data) {
                    $scope.records = data.records;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecords();
        })
        .directive('adminWordsTable', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/word_table.html',
                controller: 'WordsTableController'
            }
        });
})(angular);