(function(a) {
    "use strict";
    a.module('kao.utils', [])
        .factory('KaoPromise', function($q) {
            function KaoPromise() {
                var defer = $q.defer();
                defer.promise.success = function(fn) {
                    defer.promise.then(function() {
                        fn.apply(this, arguments)
                    });
                    return defer.promise;
                };

                defer.promise.error = function(fn) {
                    defer.promise.then(null, function() {
                        fn.apply(this, arguments);
                    });
                    return defer.promise;
                };

                return defer;
            };
            return KaoPromise;
        })
        .directive('dynamicDirective', function($compile) {
            return {
                restrict: 'E',
                replace: true,
                link: function(scope, element, attrs) {
                    if(attrs.directive) {
                        var dom = '<'+attrs.directive+'>'+'</'+attrs.directive+'>'
                        var el = $compile(dom)(scope);
                        element.append(el);
                    }
                }
            };
        })
        .directive('transcludePlaceholder', function() {
            return {
                restrict: 'A',
                replace: true,
                controller: function($transclude) {
                    this.$transclude = $transclude;
                },
                link: function(scope, element, attrs, controller) {
                    var attach = function(clone){
                        for(var i = 0; i < clone.length; i++) {
                            var el = angular.element(clone[i]);
                            if(el.attr('fills-transclude') === attrs.transcludePlaceholder){
                                element.empty();
                                element.append(el);
                            }
                        }
                    };
                    controller.$transclude(function(clone) {
                        attach(clone);
                    });
                }
            };
        })
        .directive('kaoHeader', function() {
            return {
                restrict: 'E',
                replace: true,
                transclude: true,
                scope: {title: '@'},
                templateUrl: 'static/partials/directives/kao_header.html'
            };
        });
})(angular);