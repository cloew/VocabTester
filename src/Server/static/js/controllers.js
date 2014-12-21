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
    var rootUrl = "/api/wordlist/1/quiz";
    $http.get(rootUrl).success(function(data) {
        $scope.quiz = data.quiz;
    }).error(function(error) {
        console.log(error);
    });
    
    $scope.answer = function() {
        $http.post(rootUrl+'/answer', {'answer':$scope.quiz.question.selectedIndex}).success(function(data) {
            $scope.questionResults = data.results;
        }).error(function(error) {
            console.log(error);
        });
    }
});