'use strict';

angular.module('VocabTesterDirectives', ['ui.bootstrap', 'kao.input', 'VocabTesterServices', 'VocabNavServices'])
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
    .directive('wordLists', function() {
      return {
          restrict: 'E',
          replace: true,
          controller: function($scope, $http) {
            $http.get("/api/wordlists").success(function(data) {
                $scope.wordLists = data.lists;
            }).error(function(error) {
                console.log(error);
            });
          },
          templateUrl: 'static/partials/directives/word_lists.html'
      }})
    .directive('wordList', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              conceptList: '='
          },
          controller: function($scope, $location) {
              $scope.header = 'words';
              $scope.isWords = true;
              $scope.startQuiz = function() {
                $location.path('/wordlist/'+$scope.conceptList.id+'/quiz/');
              };
          },
          templateUrl: 'static/partials/directives/concept_list.html'
      }})
    .directive('symbolLists', function() {
      return {
          restrict: 'E',
          replace: true,
          controller: function($scope, $http) {
            $http.get("/api/symbollists").success(function(data) {
                $scope.symbolLists = data.lists;
            }).error(function(error) {
                console.log(error);
            });
          },
          templateUrl: 'static/partials/directives/symbol_lists.html'
      }})
    .directive('symbolList', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              conceptList: '='
          },
          controller: function($scope, $location) {
              $scope.header = 'symbols';
              $scope.isWords = false;
              $scope.startQuiz = function() {
                $location.path('/symbollist/'+$scope.conceptList.id+'/quiz/');
              };
          },
          templateUrl: 'static/partials/directives/concept_list.html'
      }})
    .directive('conceptCount', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              conceptList: '=',
              header: '=',
              isWords: '='
          },
          controller: function($scope) {
              $scope.isOpen = false;
          },
          templateUrl: 'static/partials/directives/concept_count.html'
      }})
    .directive('conceptTable', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              concepts: '=',
              isWords: '='
          },
          controller: function($scope, conceptTableService) {
              var loadTable = function() {
                  if ($scope.concepts !== undefined) {
                      var table = conceptTableService.buildEntries($scope.concepts, $scope.isWords);
                      $scope.entries = table.entries;
                      $scope.columns = table.columns;
                  }
              }
              loadTable();
              $scope.$watch('concepts', function() {
                  loadTable();
              });
              
              
          },
          templateUrl: 'static/partials/directives/concept_table.html'
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
      }})
    .directive('info', function() {
      return {
          restrict: 'E',
          replace: true,
          controller: function($scope, $location, userService) {
              $scope.toRegister = function() {
                $location.path('/register/');
              };
          },
          templateUrl: 'static/partials/directives/info.html'
      }})