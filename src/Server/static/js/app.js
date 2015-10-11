$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("VocabTester", ["ui.bootstrap", "ngRoute", "Header", "Concepts", "Words", "quiz", "kao.auth", "kao.crud.api", "vocab.nav", "vocab.rest"]).config(["$routeProvider", "NavConfigProvider", function($routeProvider, navConfig) {
    for (var $__0 = navConfig.routes[$traceurRuntime.toProperty(Symbol.iterator)](),
        $__1; !($__1 = $__0.next()).done; ) {
      var route = $__1.value;
      {
        $routeProvider.when(route.path, route);
      }
    }
    $routeProvider.otherwise({redirectTo: "/"});
  }]).controller("IndexController", function($scope, UserService) {
    $scope.isLoggedIn = UserService.isLoggedIn;
  }).directive("info", function() {
    return {
      restrict: "E",
      replace: true,
      templateUrl: "static/partials/directives/info.html"
    };
  });
  return {};
});
