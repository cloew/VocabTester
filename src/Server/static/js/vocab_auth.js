$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("vocab.auth", ["kao.auth", "vocab.nav"]).config(["AuthConfigProvider", "NavConfigProvider", function(authConfig, navConfig) {
    authConfig.configure({
      loginRoute: navConfig.config.login.path,
      loginApi: "/api/login",
      usersApi: "/api/users",
      currentUserApi: "/api/users/current"
    });
  }]);
  return {};
});
