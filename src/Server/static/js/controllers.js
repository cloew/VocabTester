'use strict';

var controllers = angular.module('VocabTesterControllers', ['ui.bootstrap', 'Concepts', 'kao.auth']);

controllers.controller('IndexController', function ($scope, userService) {
    $scope.isLoggedIn = userService.isLoggedIn;
});;