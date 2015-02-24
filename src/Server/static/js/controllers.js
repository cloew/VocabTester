'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap', 'VocabTesterServices', 'kao.auth']);

controllers.controller('IndexController', function ($scope, userService) {
    $scope.isLoggedIn = userService.isLoggedIn;
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