'use strict';

/**
 * @ngdoc function
 * @name frontApp.controller:DrinksCtrl
 * @description
 * # DrinksCtrl
 * Controller of the frontApp
 */
angular.module('frontApp')
  .controller('DrinksCtrl', function ($scope) {
      $scope.drins = [
          {
              name: 'asd',
              icon: 'sfsdf'
          },
          {
              name: 'sd',
              icon: 'sdf'
          }
      ];
  });
