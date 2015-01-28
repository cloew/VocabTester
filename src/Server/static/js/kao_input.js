angular.module('kao.input', [])
    .directive('keyTrap', function() {
      return function(scope, elem) {
        elem.bind('keydown', function(event) {
          scope.$broadcast('keydown', event);
        });
      };
    })
    .directive('onEnterKey', function($timeout) {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 13) {
                    scope.$evalAsync(attrs.onEnterKey, {'event': event});
                    event.preventDefault();
                }
            });
        };
    })
    .directive('onUpKey', function($timeout) {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 38) {
                    scope.$evalAsync(attrs.onUpKey, {'event': event});
                    event.preventDefault();
                }
            });
        };
    })
    .directive('onDownKey', function($timeout) {
        return function(scope, element, attrs) {
            scope.$on('keydown', function(msg, event) {
                if(event.which === 40) {
                    scope.$evalAsync(attrs.onDownKey, {'event': event});
                    event.preventDefault();
                }
            });
        };
    });