'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap', 'VocabTesterServices']);

controllers.controller('WordListsController', function ($scope, $http, $location) {
    $http.get("/api/wordlists").success(function(data) {
        $scope.wordLists = data.words;
    }).error(function(error) {
        console.log(error);
    });
    
    $scope.startQuiz = function() {
        $location.path('/wordlist/'+$scope.wordLists[0].id+'/quiz/');
    };
});

controllers.controller('QuizController', function ($scope, quizService) {
    $scope.quiz = quizService.buildQuiz();
});