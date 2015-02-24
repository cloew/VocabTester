(function(a) {
    "use strict";
    a.module('Words', ['Concepts'])
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
                    $scope.startQuiz = function() {
                        $location.path('/wordlist/'+$scope.conceptList.id+'/quiz/');
                    };
                },
                templateUrl: 'static/partials/directives/concept_list.html'
            }
        })
})(angular);