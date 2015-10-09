$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("Concepts", ["ui.bootstrap", "kao.loading", "kao.table", "Language", "Forms"]).controller("LearnedFormsController", function($scope, FormsService, LanguageService, LoadingTracker) {
    var form = FormsService.current();
    $scope.formName = form.pluralName;
    $scope.quizUrl = form.randomQuizPath;
    $scope.tracker = new LoadingTracker();
    LanguageService.watchCurrentLanguage($scope, function(event, language) {
      $scope.tracker.load(form.getLearned()).success(function(data) {
        $scope.concepts = data.concepts;
        $scope.isWords = data.isWords;
      }).error(function(error) {
        console.log(error);
      });
    });
  }).directive("conceptCount", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {
        conceptList: "=",
        header: "=",
        isWords: "="
      },
      controller: function($scope) {
        $scope.isOpen = false;
      },
      templateUrl: "static/partials/directives/concept_count.html"
    };
  }).directive("conceptTable", function() {
    return {
      restrict: "E",
      replace: true,
      scope: {
        concepts: "=",
        isWords: "="
      },
      templateUrl: "static/partials/directives/concept_table.html"
    };
  });
  return {};
});
