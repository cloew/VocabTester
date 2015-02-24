'use strict';

angular.module('VocabTesterDirectives', ['ui.bootstrap', 'kao.input', 'VocabNavServices'])
    .directive('kaoTable', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              entries: '=',
              columns: '='
          },
          templateUrl: 'static/partials/directives/kao_table.html'
      }})
    .directive('headerBar', function() {
      return {
          restrict: 'E',
          replace: true,
          controller: function($scope, $location, userService) {
              $scope.toLogin = function() {
                $location.path('/login/');
              };
              $scope.toRegister = function() {
                $location.path('/register/');
              };
              $scope.logout = userService.logout;
              $scope.isLoggedIn = userService.isLoggedIn;
              userService.watchUser(function(user) {
                $scope.user = user;
              });
          },
          templateUrl: 'static/partials/directives/header.html'
      }})
    .directive('headerNav', function() {
      return {
          restrict: 'E',
          replace: true,
          controller: function($scope, $location, $route, headerNavService) {
                $scope.currentPath = $location.path();
                $scope.navSections = headerNavService;
                $scope.$on('$routeChangeSuccess', function(event, next, current) {
                    $scope.currentPath = $location.path();
                });
          },
          templateUrl: 'static/partials/directives/header_nav.html'
      }});