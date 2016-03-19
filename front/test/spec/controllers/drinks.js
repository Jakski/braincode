'use strict';

describe('Controller: DrinksCtrl', function () {

  // load the controller's module
  beforeEach(module('frontApp'));

  var DrinksCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    DrinksCtrl = $controller('DrinksCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(DrinksCtrl.awesomeThings.length).toBe(3);
  });
});
