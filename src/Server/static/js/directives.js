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
    .directive('question', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              question: '='
          },
          controller: function($scope) {
              $scope.selectOption = function(index) {
                  $scope.question.selectedIndex = index;
              };
              $scope.selectPreviousOption = function() {
                    if ($scope.question.selectedIndex === undefined) {
                        $scope.question.selectedIndex = 0;
                    }
                    else if ($scope.question.selectedIndex > 0) {
                        $scope.question.selectedIndex -= 1;
                    }
                    else {
                        $scope.question.selectedIndex = 0;
                    }
              };
              $scope.selectNextOption = function() {
                    if ($scope.question.selectedIndex === undefined) {
                        $scope.question.selectedIndex = 0;
                    }
                    else if ($scope.question.selectedIndex < ($scope.question.options.length-1)) {
                        $scope.question.selectedIndex += 1;
                    }
                    else {
                        $scope.question.selectedIndex = $scope.question.options.length-1;
                    }
              };
          },
          templateUrl: 'static/partials/directives/question.html'
      }})
    .directive('option', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              option: '='
          },
          templateUrl: 'static/partials/directives/option.html'
      }})
    .directive('quizPanel', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              quiz: '='
          },
          templateUrl: 'static/partials/directives/quiz_panel.html'
      }})
    .directive('quizResults', function() {
      return {
          restrict: 'E',
          replace: true,
          scope: {
              quiz: '='
          },
          controller: function($scope, $location, quizResultsTableService) {
              $scope.table = quizResultsTableService.buildEntries($scope.quiz);
              $scope.back = function() {
                $location.path($scope.quiz.returnTo);
              };
          },
          templateUrl: 'static/partials/directives/quiz_results.html'
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
          controller: function($scope, $location, $route, navService) {
                $scope.currentPath = $location.path();
                $scope.navSections = navService.getHeaderNav();
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