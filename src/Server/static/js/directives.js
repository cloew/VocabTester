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