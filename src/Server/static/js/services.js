'use strict';

var services = angular.module('VocabTesterServices', []);

services.factory('quizService', function($http, $routeParams) {
    function Quiz(wordListId) {
        this.wordListId = wordListId;
        this.quiz = undefined;
        this.currentQuestionIndex = 0;
        
        var self = this;
        $http.get('/api/wordlist/'+self.wordListId+'/quiz').success(function(data) {
            self.quiz = data.quiz;
            self.currentQuestion =  self.quiz.questions[self.currentQuestionIndex];
        }).error(function(error) {
            console.log(error);
        });
    };
    
    Quiz.prototype.answer = function() {
        this.currentQuestion.results = {"correct":this.currentQuestion.selectedIndex == this.currentQuestion.answerIndex};
    };
    
    Quiz.prototype.next = function() {
        this.currentQuestionIndex = this.currentQuestionIndex+1;
        this.currentQuestion =  this.quiz.questions[this.currentQuestionIndex];
    };
    
    return {
        buildQuiz: function () {
            return new Quiz($routeParams.wordlistId);
        }
    };
});