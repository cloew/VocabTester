(function(a) {
    "use strict";
    a.module('kao.table', [])
        .directive('kaoTable', function() {
            return {
            restrict: 'E',
            replace: true,
            scope: {
                entries: '=',
                columns: '='
            },
            templateUrl: 'static/partials/directives/kao_table.html'
            }
        });
})(angular);