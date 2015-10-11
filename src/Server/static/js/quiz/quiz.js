$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("quiz", ["question", "autofocus", "ui.bootstrap", "kao.input", "kao.loading", "kao.table", "Concepts", "vocab.nav"]).factory("quizService", function($http, NavService, LanguageService, OptionsQuestion, PromptQuestion, LoadingTracker) {
    function Quiz() {
      this.quiz = void 0;
      this.currentQuestionIndex = 0;
      this.correctAnswers = 0;
      this.returnTo = NavService.current().returnTo;
      this.tracker = new LoadingTracker();
      var self = this;
      LanguageService.withCurrentLanguage(function(language) {
        self.tracker.load(language.getQuiz()).success(function(data) {
          self.quiz = data.quiz;
          self.questions = [];
          self.numberOfQuestions = self.quiz.questions.length;
          for (var $__0 = self.quiz.questions[$traceurRuntime.toProperty(Symbol.iterator)](),
              $__1; !($__1 = $__0.next()).done; ) {
            var question = $__1.value;
            {
              if (question.questionType === "options") {
                self.questions.push(new OptionsQuestion(question));
              } else {
                if (question.questionType === "prompt") {
                  self.questions.push(new PromptQuestion(question));
                }
              }
            }
          }
          self.currentQuestion = self.questions[self.currentQuestionIndex];
        }).error(function(error) {
          console.log(error);
        });
      });
    }
    Quiz.prototype.answer = function() {
      var question = this.currentQuestion;
      var self = this;
      if (question.canSubmit()) {
        var correct = question.isCorrect();
        self.grading = true;
        $http.post(question.answerUrl, {"correct": correct}).success(function(data) {
          question.results = {"correct": correct};
          if (correct) {
            self.correctAnswers += 1;
          }
          question.subject.foreign.mastery = data.rating;
          self.grading = false;
        }).error(function(error) {
          console.log(error);
        });
      }
    };
    Quiz.prototype.next = function() {
      this.currentQuestionIndex = this.currentQuestionIndex + 1;
      this.currentQuestion = this.questions[this.currentQuestionIndex];
      this.completed = this.currentQuestionIndex === this.questions.length;
    };
    Quiz.prototype.canSubmit = function() {
      return !!(!!this.currentQuestion && !!this.currentQuestion.canSubmit()) && !this.grading;
    };
    return {buildQuiz: function() {
        return new Quiz();
      }};
  }).controller("QuizController", function($scope, quizService) {
    $scope.quiz = quizService.buildQuiz();
  }).directive("quizPanel", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {quiz: "="},
      templateUrl: "static/partials/directives/quiz_panel.html"
    };
  }).directive("quizResults", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {quiz: "="},
      templateUrl: "static/partials/directives/quiz_results.html"
    };
  }).directive("quizBackButton", function() {
    return {
      restrict: "E",
      replace: true,
      controller: function($scope, $element, $timeout) {
        $scope.click = function() {
          $timeout(function() {
            angular.element($element)[0].click();
          }, 0);
        };
      },
      templateUrl: "static/partials/directives/quiz_back_button.html"
    };
  });
  return {};
});
