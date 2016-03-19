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
    $scope.selected = [];
    $scope.pickItem = function (item) {
        var itemSrc = item.originalEvent.target.getAttribute('src');
        if ($scope.selected.indexOf(itemSrc) === -1) {
            $scope.selected.push(itemSrc);
            item.originalEvent.target.style = "opacity: 0.4; border: 2px solid green";
            console.log($scope.selected);
        } else {
            // remove unselected item
            $scope.selected = $scope.selected.filter(function(val) {
                return val !== itemSrc;
            });
            console.log($scope.selected);
            item.originalEvent.target.style = "opacity: 1";
        }
    }
  });
