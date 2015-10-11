$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("quiz", ["question", "autofocus", "ui.bootstrap", "kao.input", "kao.loading", "kao.table", "Concepts", "vocab.nav"]).factory("Quiz", function($http, NavService, LanguageService, QuestionFactory, LoadingTracker) {
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
          self.questions = QuestionFactory.buildAll(self.quiz.questions);
          self.numberOfQuestions = self.quiz.questions.length;
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
    return Quiz;
  }).controller("QuizController", function($scope, Quiz) {
    $scope.quiz = new Quiz();
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
