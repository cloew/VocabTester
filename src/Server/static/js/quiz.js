(function(a) {
    "use strict";
    a.module('Quiz', ['autofocus', 'ui.bootstrap', 'kao.input', 'kao.loading', 'kao.table', 'Concepts', 'vocab.nav'])
        .factory('OptionsQuestion', function() {
            function OptionsQuestion(question) {
                this.question = question;
                this.answerIndex = question.answerIndex;
                this.answerUrl = question.answerUrl;
                this.queryWord = question.queryWord;
                this.options = question.options;
                this.subject = question.subject;
                this.type = question.questionType;
            };
            OptionsQuestion.prototype.isCorrect = function() {
                return this.selectedIndex == this.question.answerIndex;
            };
            OptionsQuestion.prototype.canSubmit = function() {
                return this.selectedIndex >= 0;
            };
            
            return OptionsQuestion;
        })
        .factory('PromptQuestion', function() {
            function PromptQuestion(question) {
                this.question = question;
                this.answerUrl = question.answerUrl;
                this.prompt = question.prompt;
                this.answer = question.answer;
                this.displayAnswer = question.displayAnswer;
                this.subject = question.subject;
                this.type = question.questionType;
            };
            PromptQuestion.prototype.isCorrect = function() {
                return this.enteredText.toLowerCase() == this.question.answer;
            };
            PromptQuestion.prototype.canSubmit = function() {
                return this.enteredText;
            };
            
            return PromptQuestion;
        })
        .factory('quizService', function($http, NavService, LanguageService, OptionsQuestion, PromptQuestion, LoadingTracker) {
            function Quiz() {
                this.quiz = undefined;
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
                        for (var i = 0; i < self.numberOfQuestions; i++) {
                            var question = self.quiz.questions[i];
                            if (question.questionType === 'options') {
                                self.questions.push(new OptionsQuestion(question));
                            } else if (question.questionType === 'prompt') {
                                self.questions.push(new PromptQuestion(question));
                            }
                        }
                        self.currentQuestion =  self.questions[self.currentQuestionIndex];
                    }).error(function(error) {
                        console.log(error);
                    });
                });
            };
            Quiz.prototype.answer = function() {
                var question = this.currentQuestion;
                var self = this;
                if (question.canSubmit()) {
                    var correct = question.isCorrect();
                    self.grading = true;
                    $http.post(question.answerUrl, {'correct':correct}).success(function(data) {
                        question.results = {"correct":correct};
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
                this.currentQuestionIndex = this.currentQuestionIndex+1;
                this.currentQuestion =  this.questions[this.currentQuestionIndex];
                this.completed = (this.currentQuestionIndex == this.questions.length);
            };
            Quiz.prototype.canSubmit = function() {
                return this.currentQuestion && this.currentQuestion.canSubmit() && !this.grading;
            };
            
            return {
                buildQuiz: function () {
                    return new Quiz();
                }
            };
        })
        .factory('quizResultsTableService', function(conceptTableService) {
            return {
                buildEntries: function (quiz) {
                    var concepts = [];
                    for (var i = 0; i < quiz.questions.length; i++) {
                        var question = quiz.questions[i];
                        concepts.push(question.subject);
                    }
                    var table = conceptTableService.buildEntries(concepts, quiz.isWords);
                    for (var i = 0; i < quiz.questions.length; i++) {
                        var question = quiz.questions[i];
                        if (question.results.correct) {
                            table.entries[i].rowClass = 'success';
                        }
                        else {
                            table.entries[i].rowClass = 'danger';
                        }
                    }
                    return table;
                }
            };
        })
        .controller('QuizController', function ($scope, quizService) {
            $scope.quiz = quizService.buildQuiz();
        })
        .directive('question', function() {
          return {
              restrict: 'E',
              replace: true,
              scope: {
                  question: '='
              },
              templateUrl: 'static/partials/directives/question.html'
          }})
        .directive('optionsQuestion', function() {
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
              templateUrl: 'static/partials/directives/options_question.html'
          }})
        .directive('promptQuestion', function() {
          return {
              restrict: 'E',
              replace: true,
              scope: {
                  question: '='
              },
              templateUrl: 'static/partials/directives/prompt_question.html'
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
              controller: function($scope, quizResultsTableService) {
                  $scope.table = quizResultsTableService.buildEntries($scope.quiz);
              },
              templateUrl: 'static/partials/directives/quiz_results.html'
          }})
        .directive('quizBackButton', function() {
          return {
              restrict: 'E',
              replace: true,
              controller: function($scope, $element, $timeout) {
                  $scope.click = function() {
                    $timeout(function() {
                        a.element($element)[0].click();
                    }, 0);
                  };
              },
              templateUrl: 'static/partials/directives/quiz_back_button.html'
          }});
})(angular);