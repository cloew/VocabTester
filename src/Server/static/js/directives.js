'use strict';

angular.module('VocabTesterDirectives', ['ui.bootstrap'])
    .directive('wordCount', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              words: '=words'
          },
          link: function(scope, elements, attrs) {
              scope.isOpen = false;
          },
          templateUrl: 'static/partials/directives/word_count.html'
      }})
    .directive('question', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              question: '=question'
          },
          link: function(scope, elements, attrs) {
              scope.selectOption = function(index) {
                  scope.question.selectedIndex = index;
              };
          },
          templateUrl: 'static/partials/directives/question.html'
      }})
    .directive('option', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              option: '=option'
          },
          templateUrl: 'static/partials/directives/option.html'
      }})