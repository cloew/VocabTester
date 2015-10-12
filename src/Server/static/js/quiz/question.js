$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("question", ["autofocus", "kao.input"]).service("QuestionFactory", function(OptionsQuestion, PromptQuestion) {
    var questionCls = {
      "options": OptionsQuestion,
      "prompt": PromptQuestion
    };
    this.build = function(questionJson) {
      return new questionCls[questionJson.questionType](questionJson);
    };
    this.buildAll = function(questionsJson) {
      var questions = [];
      for (var $__0 = questionsJson[$traceurRuntime.toProperty(Symbol.iterator)](),
          $__1; !($__1 = $__0.next()).done; ) {
        var question = $__1.value;
        {
          questions.push(this.build(question));
        }
      }
      return questions;
    };
  }).factory("OptionsQuestion", function() {
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
    OptionsQuestion.prototype.buildAnswer = function() {
      return {
        type: this.type,
        guess: this.selectedIndex,
        answer: this.answerIndex
      };
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
    PromptQuestion.prototype.buildAnswer = function() {
      return {
        type: this.type,
        guess: this.enteredText,
        answer: this.answer
      };
    };
    PromptQuestion.prototype.canSubmit = function() {
      return this.enteredText;
    };
    return PromptQuestion;
  }).factory("AnswerHelper", function($http) {
    function AnswerHelper(question) {
      this.question = question;
    }
    AnswerHelper.prototype.answer = function() {
      var self = this;
      var answer = this.question.buildAnswer();
      return $http.post(this.question.answerUrl, answer).success(function(data) {
        self.question.results = data.results;
        self.question.subject.foreign.mastery = data.rating;
      });
    };
    return AnswerHelper;
  }).directive("question", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {question: "="},
      templateUrl: "static/partials/directives/quiz/questions/question.html"
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
      templateUrl: "static/partials/directives/quiz/questions/options_question.html"
    };
  }).directive("promptQuestion", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {question: "="},
      templateUrl: "static/partials/directives/quiz/questions/prompt_question.html"
    };
  }).directive("option", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {option: "="},
      templateUrl: "static/partials/directives/quiz/questions/option.html"
    };
  });
  return {};
});
