(function(a) {
    "use strict";
    a.module('kao.loading', [])
        .directive('spinner', function() {
            return {
                restrict: 'E',
                replace: true,
                template: '<div class="spinner-loader">Loading…</div>'
            }
        })
        .directive('loadingDiv', function() {
            return {
                restrict: 'E',
                replace: true,
                transclude: true,
                scope: {
                    loading: '@'
                },
                controller: function($scope) {
                    $scope.isLoading = true;
                },
                templateUrl: 'static/partials/directives/loading_div.html'
            }
        });
})(angular);