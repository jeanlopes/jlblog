/**
 * Created by jean on 13/06/14.
 */

define(['app'], function (app) {

    app.directive('checkLogged',['$animate', 'AuthenticationService', function ($animate, $authService) {

        return {
            transclude: 'element',
            priority: 600,
            restrict: 'A',
            $$tlb: true,
            link: function ($scope, $element, $attr, ctrl, $transclude) {
                var block, childScope, previousElements;
                if ($authService.isLogged()) {
                    if (!childScope) {
                      $transclude(function (clone, newScope) {
                        childScope = newScope;
                        clone[clone.length++] = document.createComment(' end check-logged ');

                        block = {
                          clone: clone
                        };
                        $animate.enter(clone, $element.parent(), $element);
                      });
                    }
                  } else {
                    if(previousElements) {
                      previousElements.remove();
                      previousElements = null;
                    }
                    if(childScope) {
                      childScope.$destroy();
                      childScope = null;
                    }
                    if(block) {
                      previousElements = getBlockElements(block.clone);
                      $animate.leave(previousElements, function() {
                        previousElements = null;
                      });
                      block = null;
                    }
                  }

            }
        }
    }]);
});