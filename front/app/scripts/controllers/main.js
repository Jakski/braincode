'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontApp
 */
angular.module('frontApp')
  .controller('MainCtrl', function ($scope) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $scope.selected = [];
    $scope.pickItem = function (item) {
        if ($scope.selected.indexOf(item.originalEvent.target.getAttribute('src')) ) {
            $scope.selected.push(item.originalEvent.target.getAttribute('src'));
            console.log($scope.selected);
        }
    }
  });
