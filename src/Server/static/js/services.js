'use strict';

var services = angular.module('VocabTesterServices', []);


services.factory('wordTableService', function() {
    return {
        buildEntries: function (words, nativeWords) {
            var table = {'entries':[], columns:[{'name':'Word', 'path':'word'}, {'name':'Native', 'path':'native'}, {'name':'Mastery', 'path':'mastery'}]};
            for (var i = 0; i < words.length; i++) {
                table.entries.push({'word':words[i].text, 'native':nativeWords[i].text, 'mastery':words[i].mastery});
            }
            return table;
        }
    };
});

services.factory('quizResultsTableService', function(wordTableService) {
    return {
        buildEntries: function (quiz) {
            var words = [];
            var nativeWords = [];
            for (var i = 0; i < quiz.quiz.questions.length; i++) {
                var question = quiz.quiz.questions[i];
                words.push(question.subject);
                nativeWords.push(question.nativeSubject);
            }
            var table = wordTableService.buildEntries(words, nativeWords);
            // table.columns.push({'name':'Correct', 'path':'correct'});
            for (var i = 0; i < quiz.quiz.questions.length; i++) {
                var question = quiz.quiz.questions[i];
                // table.entries[i].correct = question.results.correct;
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
        if (question.selectedIndex !== undefined) { 
            var correct = question.selectedIndex == this.currentQuestion.answerIndex;
            question.results = {"correct":correct};
            if (correct) {
                this.correctAnswers += 1;
            }
            $http.post('/api/wordlist/'+this.wordListId+'/quiz/answer', {'wordId':question.subject.id, 'correct':correct}).success(function(data) {
                question.word = data;
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
    
    return {
        buildQuiz: function () {
            return new Quiz($routeParams.wordlistId);
        }
    };
});