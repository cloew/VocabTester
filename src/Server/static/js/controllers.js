'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap', 'VocabTesterServices', 'kao.auth']);

controllers.controller('IndexController', function ($scope, userService) {
    $scope.isLoggedIn = userService.isLoggedIn;
});

controllers.controller('LoginController', function ($scope, $location, userService) {
    $scope.login = function() {
        userService.login($scope.email, $scope.password, function() {
            var next = $location.search().returnTo;
            if (!next) {
                next = '/'
            }
            $location.path(next);
            $location.search('returnTo', null);
        }, function(error) {
            $scope.errorMessage = error.message;
        });
    };
});

controllers.controller('RegisterController', function ($scope, $location, userService) {
    $scope.register = function() {
        userService.register($scope, function() {
            $location.path('/');
        }, function(error) {
            $scope.errorMessage = error.message;
        });
    };
});

controllers.controller('QuizController', function ($scope, quizService) {
    $scope.quiz = quizService.buildQuiz();
});

controllers.controller('LearnedFormsController', function ($scope, $http, $location) {
    $http.get('/api'+$location.path()).success(function(data) {
            $scope.concepts = data.concepts;
            $scope.isWords = data.isWords;
        }).error(function(error) {
            console.log(error);
        });
    $scope.goTo = function(path) {
        $location.path(path);
    }
});