'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap', 'VocabTesterServices']);

controllers.controller('WordListsController', function ($scope, $http, $location) {
    $http.get("/api/wordlists").success(function(data) {
        $scope.wordLists = data.words;
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('LoginController', function ($scope, $http) {
    $scope.login = function() {
        if ($scope.loginForm.$valid) {
            $http.post('/api/login', {'email':$scope.email, 'password':$scope.password}).success(function(data) {
                console.log(data);
            }).error(function(error) {
                console.log(error);
            });
        }
    };
});

controllers.controller('QuizController', function ($scope, quizService) {
    $scope.quiz = quizService.buildQuiz();
});