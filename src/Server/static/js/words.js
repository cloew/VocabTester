(function(a) {
    "use strict";
    a.module('Words', ['Concepts'])
        .controller('SearchController', function ($scope, $http, LanguageService) {
            $scope.results = undefined;
            $scope.isWords = true;
            $scope.search = function(text) {
                LanguageService.withCurrentLanguage(function(language) {
                    language.search({'text':text}).success(function(data) {
                        $scope.results = data.results;
                    }).error(function(error) {
                        console.log(error);
                    });
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