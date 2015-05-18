(function(a) {
    "use strict";
    a.module('Symbols', ['Concepts', 'Language'])
        .directive('symbolLists', function() {
            return {
                restrict: 'E',
                replace: true,
                controller: function($scope, LanguageService) {
                    LanguageService.withCurrentLanguage(function(language) {
                        language.getSymbolLists().success(function(data) {
                            $scope.symbolLists = data.lists;
                        }).error(function(error) {
                            console.log(error);
                        });
                    });
                },
                templateUrl: 'static/partials/directives/symbol_lists.html'
            }
        })
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
                    $scope.quizUrl = '#/symbollist/'+$scope.conceptList.id+'/quiz/';
                },
                templateUrl: 'static/partials/directives/concept_list.html'
            }
        });
})(angular);