$traceurRuntime.ModuleStore.getAnonymousModule(function() {
  "use strict";
  angular.module("vocab.auth.controllers", ["kao.loading", "kao.utils", "kao.nav"]).controller("LoginController", function($scope, $location, UserService, NavService) {
    $scope.login = function() {
      UserService.login({
        "email": $scope.email,
        "password": $scope.password
      }).success(function(user) {
        var next = $location.search().returnTo;
        if (!next) {
          next = NavService.wordLists.path;
        }
        $location.path(next);
        $location.search("returnTo", null);
      }).error(function(error) {
        $scope.errorMessage = error.message;
      });
    };
  }).controller("RegisterController", function($scope, UserService, NavService) {
    $scope.user = {};
    $scope.register = function() {
      UserService.register($scope.user).success(function(user) {
        NavService.enroll.goTo();
      }).error(function(error) {
        $scope.errorMessage = error.message;
      });
    };
  }).controller("ProfileController", function($scope, UserService, LanguageEnrollmentsService) {
    $scope.user = {};
    LanguageEnrollmentsService.requestEnrollments(function(enrollments) {
      $scope.enrollments = enrollments;
    });
    UserService.withUser().success(function(user) {
      angular.copy(user, $scope.user);
    }).error(function(error) {
      console.log(error);
    });
    $scope.update = function() {
      UserService.update($scope.user).success(function(user) {}).error(function(error) {
        $scope.errorMessage = error.message;
      });
    };
  }).controller("ChooseEnrollmentController", function($scope, languages, UserService, LanguageEnrollmentsService, NavService, LoadingTracker) {
    $scope.languages = [];
    $scope.tracker = new LoadingTracker();
    UserService.withUser().success(function(user) {
      $scope.tracker.load(languages()).success(function(data) {
        LanguageEnrollmentsService.requestEnrollments(function(enrollments) {
          var enrolledLanguageIds = [];
          angular.forEach(enrollments, function(enrollment, key) {
            enrolledLanguageIds.push(enrollment.language.id);
          });
          angular.forEach(data.records, function(language, key) {
            if (!!(language.id !== user.nativeLanguage.id) && !!(enrolledLanguageIds.indexOf(language.id) === -1)) {
              $scope.languages.push(language);
            }
          });
        });
      }).error(function(error) {
        console.log(error);
      });
    }).error(function(error) {
      console.log(error);
    });
    $scope.enroll = function(language) {
      LanguageEnrollmentsService.create(language).then(function(data) {
        NavService.profile.goTo();
      }, function(error) {
        console.log(error);
      });
    };
  }).factory("LanguageEnrollmentsService", function($http, $q, $rootScope, $timeout, KaoDefer, userEvents) {
    var service = {
      currentChangedEventType: "current-enrollment-changed",
      enrollmentsChangedEventType: "enrollments-changed",
      loadEnrollments: function(callback) {
        var self = this;
        $http.get("/api/users/current/enrollments").success(function(data) {
          self.enrollments = data.enrollments;
          callback(self.enrollments);
        }).error(function(error) {
          console.log(error);
        });
      },
      enrollments: void 0,
      requestEnrollments: function(callback) {
        if (!(typeof this.enrollments !== "undefined" && this.enrollments !== null)) {
          this.loadEnrollments(callback);
        } else {
          callback(this.enrollments);
        }
      },
      watchEnrollments: function(scope, callback) {
        scope.$on(this.enrollmentsChangedEventType, callback);
        this.requestEnrollments(function(enrollments) {
          callback(void 0, enrollments);
        });
      },
      withCurrentEnrollment: function() {
        var deferred = KaoDefer();
        var findCurrentEnrollment = function(enrollments) {
          for (var $__0 = enrollments[$traceurRuntime.toProperty(Symbol.iterator)](),
              $__1; !($__1 = $__0.next()).done; ) {
            var enrollment = $__1.value;
            {
              if (enrollment.default) {
                deferred.resolve(enrollment);
                return;
              }
            }
          }
          deferred.reject();
        };
        var self = this;
        $timeout(function() {
          if (!(typeof self.enrollments !== "undefined" && self.enrollments !== null)) {
            self.loadEnrollments(findCurrentEnrollment);
          } else {
            findCurrentEnrollment(self.enrollments);
          }
        }, 0);
        return deferred.promise;
      },
      watchCurrentEnrollment: function(scope, callback) {
        scope.$on(this.currentChangedEventType, callback);
        this.withCurrentEnrollment().success(function(currentEnrollment) {
          callback(void 0, currentEnrollment);
        });
      },
      create: function(language, callback) {
        var deferred = $q.defer();
        var self = this;
        $http.post("/api/users/current/enrollments", {language: language}).success(function(data) {
          self.requestEnrollments(function(enrollments) {
            if (enrollments.length === 0) {
              data.record.default = true;
              $rootScope.$broadcast(self.currentChangedEventType, data.record);
            }
            enrollments.push(data.record);
            $rootScope.$broadcast(self.enrollmentsChangedEventType, enrollments);
          });
          deferred.resolve(data);
        }).error(function(error) {
          deferred.reject(error);
        });
        return deferred.promise;
      },
      changeCurrentEnrollment: function(index) {
        var self = this;
        this.withCurrentEnrollment().success(function(currentEnrollment) {
          currentEnrollment.default = false;
          self.enrollments[index].default = true;
          $rootScope.$broadcast(self.currentChangedEventType, self.enrollments[index]);
        });
      }
    };
    $rootScope.$on(userEvents.logout, function() {
      service.enrollments = void 0;
    });
    return service;
  }).service("requireEnrollment", function($location, LanguageEnrollmentsService, NavService) {
    return function(event) {
      LanguageEnrollmentsService.withCurrentEnrollment().error(function() {
        $location.path(NavService.enroll.path);
      });
    };
  });
  return {};
});
