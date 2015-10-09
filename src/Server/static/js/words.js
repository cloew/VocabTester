$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("Words", ["kao.loading", "Concepts"]).controller("SearchController", function($scope, $http, LanguageService, LoadingTracker) {
    $scope.results = void 0;
    $scope.isWords = true;
    $scope.tracker = new LoadingTracker();
    $scope.search = function(text) {
      LanguageService.withCurrentLanguage(function(language) {
        $scope.tracker.load(language.search({"text": text})).success(function(data) {
          $scope.results = data.results;
        }).error(function(error) {
          console.log(error);
        });
      });
    };
  }).directive("searchResult", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {result: "="},
      controller: function($scope, $http) {
        $scope.learn = function() {
          $http.post("/api/words/" + $scope.result.foreign.id + "/learn").success(function(data) {
            $scope.result.foreign = data.word;
          }).error(function(error) {
            console.log(error);
          });
        };
      },
      templateUrl: "static/partials/directives/search_result.html"
    };
  });
  return {};
});
