'use strict';

angular.module('VocabTesterDirectives', ['ui.bootstrap'])
    .directive('keyTrap', function() {
      return function(scope, elem) {
        elem.bind('keydown', function(event) {
          scope.$broadcast('keydown', event);
        });
      };
    })
    .directive('ngEnter', function() {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 13) {
                    scope.$apply(function(){
                        scope.$eval(attrs.ngEnter, {'event': event});
                    });
                    event.preventDefault();
                }
            });
        };
    })
    .directive('kaoTable', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              entries: '=',
              columns: '='
          },
          templateUrl: 'static/partials/directives/kao_table.html'
      }})
    .directive('wordList', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              wordList: '='
          },
          controller: function($scope, $location) {
              $scope.startQuiz = function() {
                $location.path('/wordlist/'+$scope.wordList.id+'/quiz/');
              };
          },
          templateUrl: 'static/partials/directives/word_list.html'
      }})
    .directive('wordCount', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              wordList: '='
          },
          controller: function($scope) {
              $scope.isOpen = false;
          },
          templateUrl: 'static/partials/directives/word_count.html'
      }})
    .directive('wordTable', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              words: '=',
              nativeWords: '='
          },
          controller: function($scope, wordTableService) {
              var table = wordTableService.buildEntries($scope.words, $scope.nativeWords);
              $scope.entries = table.entries;
              $scope.columns = table.columns;
          },
          templateUrl: 'static/partials/directives/word_table.html'
      }})
    .directive('question', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              question: '='
          },
          controller: function($scope) {
              $scope.selectOption = function(index) {
                  $scope.question.selectedIndex = index;
              };
          },
          templateUrl: 'static/partials/directives/question.html'
      }})
    .directive('option', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              option: '='
          },
          templateUrl: 'static/partials/directives/option.html'
      }})
    .directive('quizPanel', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              quiz: '='
          },
          templateUrl: 'static/partials/directives/quiz_panel.html'
      }})
    .directive('quizResults', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              quiz: '='
          },
          controller: function($scope, $location, quizResultsTableService) {
              $scope.table = quizResultsTableService.buildEntries($scope.quiz);
              $scope.back = function() {
                $location.path('/wordlist/');
              };
          },
          templateUrl: 'static/partials/directives/quiz_results.html'
      }})