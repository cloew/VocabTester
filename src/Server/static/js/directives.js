'use strict';

angular.module('VocabTesterDirectives', ['ui.bootstrap'])
    .directive('keyTrap', function() {
      return function(scope, elem) {
        elem.bind('keydown', function(event) {
          scope.$broadcast('keydown', event);
        });
      };
    })
    .directive('onEnterKey', function($timeout) {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 13) {
                    scope.$evalAsync(attrs.onEnterKey, {'event': event});
                    event.preventDefault();
                }
            });
        };
    })
    .directive('onUpKey', function($timeout) {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 38) {
                    scope.$evalAsync(attrs.onUpKey, {'event': event});
                    event.preventDefault();
                }
            });
        };
    })
    .directive('onDownKey', function($timeout) {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 40) {
                    scope.$evalAsync(attrs.onDownKey, {'event': event});
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
              concepts: '='
          },
          controller: function($scope, wordTableService) {
              var table = wordTableService.buildEntries($scope.concepts);
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
              $scope.selectPreviousOption = function() {
                    if ($scope.question.selectedIndex === undefined) {
                        $scope.question.selectedIndex = 0;
                    }
                    else if ($scope.question.selectedIndex > 0) {
                        $scope.question.selectedIndex -= 1;
                    }
                    else {
                        $scope.question.selectedIndex = 0;
                    }
              };
              $scope.selectNextOption = function() {
                    if ($scope.question.selectedIndex === undefined) {
                        $scope.question.selectedIndex = 0;
                    }
                    else if ($scope.question.selectedIndex < ($scope.question.options.length-1)) {
                        $scope.question.selectedIndex += 1;
                    }
                    else {
                        $scope.question.selectedIndex = $scope.question.options.length-1;
                    }
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