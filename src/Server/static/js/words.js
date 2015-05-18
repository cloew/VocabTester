(function(a) {
    "use strict";
    a.module('Words', ['Concepts'])
        .directive('wordLists', function() {
            return {
                restrict: 'E',
                replace: true,
                controller: function($scope, LanguageService) {
                    LanguageService.withCurrentLanguage(function(language) {
                        language.getWordLists().success(function(data) {
                            $scope.wordLists = data.lists;
                        }).error(function(error) {
                            console.log(error);
                        });
                    });
                },
                templateUrl: 'static/partials/directives/word_lists.html'
            }
        })
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
                    $scope.quizUrl = '#/wordlist/'+$scope.conceptList.id+'/quiz/';
                },
                templateUrl: 'static/partials/directives/concept_list.html'
            }
        })
        .controller('SearchController', function ($scope, $http) {
            $scope.results = undefined;
            $scope.isWords = true;
            $scope.search = function(text) {
                $http.post('/api/search', {'text':text}).success(function(data) {
                    $scope.results = data.results;
                    console.log($scope.results);
                }).error(function(error) {
                    console.log(error);
                });
            };
        })
        .directive('searchResult', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    result: '='
                },
                controller: function($scope, $http) {
                    $scope.learn = function() {
                        $http.post('/api/words/'+$scope.result.foreign.id+'/learn').success(function(data) {
                            $scope.result.foreign = data.word;
                        }).error(function(error) {
                            console.log(error);
                        });
                    };
                },
                templateUrl: 'static/partials/directives/search_result.html'
            }
        });
})(angular);