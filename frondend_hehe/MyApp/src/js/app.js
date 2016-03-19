angular.module('MyApp', [
  'ngRoute',
  'mobile-angular-ui.gestures',
  'mobile-angular-ui',
  'MyApp.controllers.Main'
])

.config(function($routeProvider) {
  $routeProvider.when('/', {templateUrl:'home.html',  reloadOnSearch: false});
});

app.directive('dragMe', ['$drag', function($drag){
  return {
    controller: function($scope, $element) {
      $drag.bind($element, 
        {
          // limit movement of element to its parent
          transform: $drag.TRANSLATE_INSIDE($element.parent()),

          end: function(drag) {
            // go back to initial position
            drag.reset();
          }
        },
        { // release touch when movement is outside bounduaries
          sensitiveArea: $element.parent()
        }
      );
    }
  };
}]);