(function(a) {
    "use strict";
    a.module('kao.utils', [])
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
            }
        })
        .directive('placeholder', function() {
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
                            if(el.attr('binds-to') === attrs.placeholder){
                                element.empty();
                                element.append(el);
                            }
                        }
                    };
                    controller.$transclude(function(clone) {
                        attach(clone);
                    });
                }
            }
        });
})(angular);