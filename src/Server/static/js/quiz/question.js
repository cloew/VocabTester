$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("question", ["autofocus", "ui.bootstrap", "kao.input", "kao.loading", "kao.table", "Concepts", "vocab.nav"]).factory("OptionsQuestion", function() {
    function OptionsQuestion(question) {
      for (var $__0 = Object.keys(question)[$traceurRuntime.toProperty(Symbol.iterator)](),
          $__1; !($__1 = $__0.next()).done; ) {
        var attr = $__1.value;
        {
          var value = question[attr];
          this[attr] = value;
        }
      }
      this.type = question.questionType;
    }
    OptionsQuestion.prototype.isCorrect = function() {
      return this.selectedIndex === this.answerIndex;
    };
    OptionsQuestion.prototype.canSubmit = function() {
      return this.selectedIndex >= 0;
    };
    return OptionsQuestion;
  }).factory("PromptQuestion", function() {
    function PromptQuestion(question) {
      for (var $__0 = Object.keys(question)[$traceurRuntime.toProperty(Symbol.iterator)](),
          $__1; !($__1 = $__0.next()).done; ) {
        var attr = $__1.value;
        {
          var value = question[attr];
          this[attr] = value;
        }
      }
      this.type = question.questionType;
    }
    PromptQuestion.prototype.isCorrect = function() {
      return this.enteredText.toLowerCase() === this.answer;
    };
    PromptQuestion.prototype.canSubmit = function() {
      return this.enteredText;
    };
    return PromptQuestion;
  }).directive("question", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {question: "="},
      templateUrl: "static/partials/directives/question.html"
    };
  }).directive("optionsQuestion", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {question: "="},
      controller: function($scope) {
        $scope.selectOption = function(index) {
          $scope.question.selectedIndex = index;
        };
        $scope.selectPreviousOption = function() {
          if (!(typeof $scope.question.selectedIndex !== "undefined" && $scope.question.selectedIndex !== null)) {
            $scope.question.selectedIndex = 0;
          } else {
            if ($scope.question.selectedIndex > 0) {
              $scope.question.selectedIndex -= 1;
            } else {
              $scope.question.selectedIndex = 0;
            }
          }
        };
        $scope.selectNextOption = function() {
          if (!(typeof $scope.question.selectedIndex !== "undefined" && $scope.question.selectedIndex !== null)) {
            $scope.question.selectedIndex = 0;
          } else {
            if ($scope.question.selectedIndex < $scope.question.options.length - 1) {
              $scope.question.selectedIndex += 1;
            } else {
              $scope.question.selectedIndex = $scope.question.options.length - 1;
            }
          }
        };
      },
      templateUrl: "static/partials/directives/options_question.html"
    };
  }).directive("promptQuestion", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {question: "="},
      templateUrl: "static/partials/directives/prompt_question.html"
    };
  }).directive("option", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {option: "="},
      templateUrl: "static/partials/directives/option.html"
    };
  });
  return {};
});
