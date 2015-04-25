(function(a) {
    'use strict';
    a.module('kao.rest', [])
        .controller('ListController', function ($scope, $http, $location, navService) {
            $scope.records = [];
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.delete = function(id) {
                $http.delete(navService.getApiUrl() + '/' + id).success(function(data) {
                    $scope.getRecords();
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.getRecords = function() {
                $http.get(navService.getApiUrl()).success(function(data) {
                    $scope.records = data.records;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecords();
        })
        .controller('NewController', function ($scope, $http, navService) {
            $scope.record = {};
            
            $scope.create = function() {
                $http.post(navService.getApiUrl(), $scope.record).success(function(data) {
                    
                }).error(function(error) {
                    console.log(error);
                });
            };
        })
        .directive('languageForm', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/language_form.html'
            }
        });
})(angular);