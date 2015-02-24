'use strict';

var services = angular.module('VocabTesterServices', ['VocabNavServices']);

services.factory('conceptTableService', function() {
    return {
        buildEntries: function (concepts, isWords) {
            var columns = [];
            
            if (isWords) {
                columns.push({'name':'Word', 'path':'form'});
            }
            else {
                columns.push({'name':'Symbol', 'path':'form'});
            }
            columns.push({'name':'Native', 'path':'native'});
            columns.push({'name':'Mastery', 'path':'mastery'});
            
            var table = {'entries':[], columns:columns};
            for (var i = 0; i < concepts.length; i++) {
                table.entries.push({'form':concepts[i].foreign.text, 'native':concepts[i].native.text, 'mastery':concepts[i].foreign.mastery});
            }
            return table;
        }
    };
});

services.factory('quizResultsTableService', function(conceptTableService) {
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
});

services.factory('quizService', function($http, $location, $routeParams, navService) {
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
});