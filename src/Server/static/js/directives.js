'use strict';

angular.module('VocabTesterDirectives', ['ui.bootstrap'])
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
              words: '='
          },
          controller: function($scope) {
              $scope.isOpen = false;
          },
          templateUrl: 'static/partials/directives/word_count.html'
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
          controller: function($scope, $location) {
              $scope.back = function() {
                $location.path('/wordlist/');
              };
          },
          templateUrl: 'static/partials/directives/quiz_results.html'
      }})