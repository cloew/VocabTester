'use strict';

var services = angular.module('VocabTesterServices', []);

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
        var correct = this.currentQuestion.selectedIndex == this.currentQuestion.answerIndex;
        this.currentQuestion.results = {"correct":correct};
        if (correct) {
            this.correctAnswers += 1;
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