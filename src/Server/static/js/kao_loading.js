(function(a) {
    "use strict";
    a.module('kao.loading', ['kao.utils'])
        .factory('LoadingTracker', function(KaoPromise) {
            function LoadingTracker() {
                this.isLoading = false;
            };
            LoadingTracker.prototype.load = function(promise) {
                this.isLoading = true;
                var deferred = KaoPromise();
                var self = this;
                
                promise.then(deferred.resolve, deferred.reject);
                deferred.promise.finally(null).finally(function() {
                    self.isLoading = false;
                });
                
                return deferred.promise;
            };
            return LoadingTracker;
        })
        .service('LoadingTrackerService', function(LoadingTracker) {
            var trackers = {};
            return {
                get: function(name) {
                    var tracker = trackers[name];
                    if (tracker === undefined) {
                        tracker = new LoadingTracker();
                        trackers[name] = tracker;
                    }
                    return tracker;
                }
            };
        })
        .directive('spinner', function() {
            return {
                restrict: 'E',
                replace: true,
                template: '<div class="spinner-loader">Loading…</div>'
            };
        })
        .directive('loadingDiv', function() {
            return {
                restrict: 'E',
                replace: true,
                transclude: true,
                scope: {
                    loading: '@'
                },
                controller: function($scope, LoadingTrackerService, $timeout) {
                    $scope.tracker = LoadingTrackerService.get($scope.loading);
                },
                templateUrl: 'static/partials/directives/loading_div.html'
            };
        });
})(angular);