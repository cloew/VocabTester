'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap']);

controllers.controller('WordListsController', function ($scope, $http) {
    $http.get("/api/wordlists").success(function(data) {
        $scope.wordLists = data.words;
    }).error(function(error) {
        console.log(error);
    });
});