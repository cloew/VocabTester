$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("quiz", ["question", "ui.bootstrap", "kao.input", "kao.loading", "kao.table", "Concepts", "vocab.nav"]).factory("Quiz", function(NavService, LanguageService, QuestionFactory, AnswerHelper, LoadingTracker) {
    function Quiz() {
      this.quiz = void 0;
      this.currentQuestionIndex = 0;
      this.correctAnswers = 0;
      this.returnTo = NavService.current().returnTo;
      this.tracker = new LoadingTracker();
      this.gradeTracker = new LoadingTracker();
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
      var self = this;
      var question = this.currentQuestion;
      if (question.canSubmit()) {
        this.gradeTracker.load(new AnswerHelper(question).answer()).success(function(data) {
          if (question.results.correct) {
            self.correctAnswers += 1;
          }
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
      templateUrl: "static/partials/directives/quiz/quiz_panel.html"
    };
  }).directive("quizHeader", function() {
    return {
      restrict: "E",
      replace: true,
      template: "<div>     <span class=\"pull-right question-progress\" ng-if=\"quiz.completed\">{{quiz.correctAnswers}} of {{quiz.numberOfQuestions}}</span>     <span class=\"pull-right question-progress\" ng-if=\"!quiz.completed\" ng-show=\"quiz.quiz.questions\">{{quiz.currentQuestionIndex+1}} of {{quiz.quiz.questions.length}}</span>     <h3 class=\"panel-title\">{{quiz.quiz.name}} Quiz</h3> </div>"
    };
  }).directive("quizBody", function() {
    return {
      restrict: "E",
      replace: true,
      template: "<div><loading-div tracker=\"quiz.tracker\">     <question question=\"quiz.currentQuestion\"></question> </loading-div></div>"
    };
  }).directive("quizResults", function() {
    return {
      restrict: "E",
      replace: true,
      templateUrl: "static/partials/directives/quiz/quiz_results.html"
    };
  }).directive("answerButton", function() {
    return {
      restrict: "E",
      replace: true,
      template: "<div>     <loading-button class=\"pull-right btn btn-primary quiz-button\" tracker=\"quiz.gradeTracker\" data-loading-text=\"Grading...\" on-enter-key=\"quiz.answer();\" ng-click=\"quiz.answer();\" ng-disabled=\"!quiz.canSubmit();\">Submit</loading-button> </div>"
    };
  }).directive("nextQuestionButton", function() {
    return {
      restrict: "E",
      replace: true,
      template: "<button class=\"pull-right btn btn-success quiz-button\" on-enter-key=\"quiz.next();\" ng-click=\"quiz.next();\">Next</button>"
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
      template: "<a ng-href=\"#{{quiz.returnTo}}\" class=\"pull-right btn btn-success quiz-button\" on-enter-key=\"click();\">Back</a>"
    };
  });
  return {};
});
