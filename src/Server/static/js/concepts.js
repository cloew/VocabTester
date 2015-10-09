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
  }).factory("conceptTableService", function() {
    return {buildEntries: function(concepts, isWords) {
        var columns = [];
        if (isWords) {
          columns.push({
            "name": "Word",
            "path": "form"
          });
        } else {
          columns.push({
            "name": "Symbol",
            "path": "form"
          });
        }
        columns.push({
          "name": "Native",
          "path": "native"
        });
        columns.push({
          "name": "Mastery",
          "path": "mastery"
        });
        var table = {
          "entries": [],
          columns: columns
        };
        for (var $__0 = concepts[$traceurRuntime.toProperty(Symbol.iterator)](),
            $__1; !($__1 = $__0.next()).done; ) {
          var concept = $__1.value;
          {
            table.entries.push({
              "form": concept.foreign.text,
              "native": concept.native.text,
              "mastery": concept.foreign.mastery
            });
          }
        }
        return table;
      }};
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
      controller: function($scope, conceptTableService) {
        var loadTable = function() {
          if (typeof $scope.concepts !== "undefined" && $scope.concepts !== null) {
            var table = conceptTableService.buildEntries($scope.concepts, $scope.isWords);
            $scope.entries = table.entries;
            $scope.columns = table.columns;
          }
        };
        loadTable();
        $scope.$watch("concepts", function() {
          loadTable();
        });
      },
      templateUrl: "static/partials/directives/concept_table.html"
    };
  });
  return {};
});
