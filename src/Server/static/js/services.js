'use strict';

var services = angular.module('VocabTesterServices', []);


services.factory('wordTableService', function() {
    return {
        buildEntries: function (concepts) {
            var table = {'entries':[], columns:[{'name':'Word', 'path':'word'}, {'name':'Native', 'path':'native'}, {'name':'Mastery', 'path':'mastery'}]};
            for (var i = 0; i < concepts.length; i++) {
                table.entries.push({'word':concepts[i].foreign.text, 'native':concepts[i].native.text, 'mastery':concepts[i].foreign.mastery});
            }
            return table;
        }
    };
});

services.factory('quizResultsTableService', function(wordTableService) {
    return {
        buildEntries: function (quiz) {
            var concepts = [];
            for (var i = 0; i < quiz.quiz.questions.length; i++) {
                var question = quiz.quiz.questions[i];
                concepts.push(question.subject);
            }
            var table = wordTableService.buildEntries(concepts);
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
});

services.factory('quizService', function($http, $routeParams) {
    function Quiz(wordListId) {
        this.wordListId = wordListId;
        this.quiz = undefined;
        this.currentQuestionIndex = 0;
        this.correctAnswers = 0;
        
        var self = this;
        $http.get('/api/wordlist/'+self.wordListId+'/quiz').success(function(data) {
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
            $http.post('/api/wordlist/'+this.wordListId+'/quiz/answer', {'wordId':question.subject.foreign.id, 'correct':correct}).success(function(data) {
                question.results = {"correct":correct};
                if (correct) {
                    self.correctAnswers += 1;
                }
                question.subject.foreign = data;
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
            return new Quiz($routeParams.wordlistId);
        }
    };
});

services.factory('userService', function($http, $window) {
    return {
        login: function (email, password, successCallback, errorCallback) {
            $http.post('/api/login', {'email':email, 'password':password}).success(function(data) {
                $window.sessionStorage.token = data.token;
                successCallback();
                return {'success': true};
            }).error(function(error) {
                console.log(error);
                errorCallback(error);
            });
        },
        register: function (params, successCallback, errorCallback) {
            $http.post('/api/register', {'email':params.email, 'password':params.password, 'givenName':params.firstName, 'lastName':params.lastName}).success(function(data) {
                $window.sessionStorage.token = data.token;
                successCallback();
                return {'success': true};
            }).error(function(error) {
                console.log(error);
                errorCallback(error);
            });
        }
    };
});