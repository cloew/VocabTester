(function(a) {
    "use strict";
    a.module('Concepts', ['ui.bootstrap', 'kao.table', 'VocabNav', 'Language', 'Forms'])
        .controller('LearnedFormsController', function ($scope, FormsService, LanguageService) {
            var form = FormsService.current();
            
            LanguageService.watchCurrentLanguage($scope, function(event, language) {
                form.getLearned().success(function(data) {
                    $scope.concepts = data.concepts;
                    $scope.isWords = data.isWords;
                }).error(function(error) {
                    console.log(error);
                });
            });
            
            $scope.formName = form.pluralName;
            $scope.quizUrl = form.randomQuizPath;
        })
        .factory('conceptTableService', function() {
            return {
                buildEntries: function (concepts, isWords) {
                    var columns = [];
                    
                    if (isWords) {
                        columns.push({'name':'Word', 'path':'form'});
                    }
                    else {
                        columns.push({'name':'Symbol', 'path':'form'});
                    }
                    columns.push({'name':'Native', 'path':'native'});
                    columns.push({'name':'Mastery', 'path':'mastery'});
                    
                    var table = {'entries':[], columns:columns};
                    for (var i = 0; i < concepts.length; i++) {
                        table.entries.push({'form':concepts[i].foreign.text, 'native':concepts[i].native.text, 'mastery':concepts[i].foreign.mastery});
                    }
                    return table;
                }
            }
        })
        .directive('conceptCount', function() {
          return {
              restrict: 'E',
              replace: true,
              scope: {
                  conceptList: '=',
                  header: '=',
                  isWords: '='
              },
              controller: function($scope) {
                  $scope.isOpen = false;
              },
              templateUrl: 'static/partials/directives/concept_count.html'
          }})
        .directive('conceptTable', function() {
          return {
              restrict: 'E',
              replace: true,
              scope: {
                  concepts: '=',
                  isWords: '='
              },
              controller: function($scope, conceptTableService) {
                  var loadTable = function() {
                      if ($scope.concepts !== undefined) {
                          var table = conceptTableService.buildEntries($scope.concepts, $scope.isWords);
                          $scope.entries = table.entries;
                          $scope.columns = table.columns;
                      }
                  }
                  loadTable();
                  $scope.$watch('concepts', function() {
                      loadTable();
                  });
              },
              templateUrl: 'static/partials/directives/concept_table.html'
          }});
})(angular);