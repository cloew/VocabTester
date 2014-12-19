'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap']);

controllers.controller('WordListsController', function ($scope, $http, $location) {
    $http.get("/api/wordlists").success(function(data) {
        $scope.wordLists = data.words;
    }).error(function(error) {
        console.log(error);
    });
    
    $scope.startQuiz = function() {
        $location.path('/wordlist/1/quiz/');
    };
});

controllers.controller('QuizController', function ($scope, $http) {
    $http.get("/api/wordlist/1/quiz").success(function(data) {
        $scope.quiz = data.quiz;
    }).error(function(error) {
        console.log(error);
    });
});