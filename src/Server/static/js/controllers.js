'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap', 'VocabTesterServices']);

controllers.controller('WordListsController', function ($scope, $http, $location) {
    $http.get("/api/wordlists").success(function(data) {
        $scope.wordLists = data.words;
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('LoginController', function ($scope, userService) {
    $scope.login = function() {
        userService.login($scope.email, $scope.password);
    };
});

controllers.controller('QuizController', function ($scope, quizService) {
    $scope.quiz = quizService.buildQuiz();
});