(function(a) {
    "use strict";
    a.module('Quiz', ['ui.bootstrap', 'kao.input', 'Concepts', 'VocabNavServices'])
        .factory('quizService', function($http, $location, $routeParams, navService) {
            function Quiz(wordListId) {
                this.wordListId = wordListId;
                this.quiz = undefined;
                this.currentQuestionIndex = 0;
                this.correctAnswers = 0;
                this.returnTo = navService.getReturnTo();
                
                var self = this;
                $http.get('/api' +$location.path()).success(function(data) {
                    self.quiz = data.quiz;
                    self.currentQuestion =  self.quiz.questions[self.currentQuestionIndex];
                    self.numberOfQuestions = self.quiz.questions.length;
                }).error(function(error) {
                    console.log(error);
                });
            };
            Quiz.prototype.answer = function() {
                var question = this.currentQuestion;
                var self = this;
                if (question.selectedIndex !== undefined) {
                    var correct = question.selectedIndex == this.currentQuestion.answerIndex;
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
                this.currentQuestion =  this.quiz.questions[this.currentQuestionIndex];
                this.completed = (this.currentQuestionIndex == this.quiz.questions.length);
            };
            Quiz.prototype.canSubmit = function() {
                return this.currentQuestion && (this.currentQuestion.selectedIndex >= 0) && !this.grading;
            };
            
            return {
                buildQuiz: function () {
                    return new Quiz($routeParams.listId);
                }
            };
        })
        .factory('quizResultsTableService', function(conceptTableService) {
            return {
                buildEntries: function (quiz) {
                    var concepts = [];
                    for (var i = 0; i < quiz.quiz.questions.length; i++) {
                        var question = quiz.quiz.questions[i];
                        concepts.push(question.subject);
                    }
                    var table = conceptTableService.buildEntries(concepts, quiz.isWords);
                    for (var i = 0; i < quiz.quiz.questions.length; i++) {
                        var question = quiz.quiz.questions[i];
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
                    $location.path($scope.quiz.returnTo);
                  };
              },
              templateUrl: 'static/partials/directives/quiz_results.html'
          }});
})(angular);