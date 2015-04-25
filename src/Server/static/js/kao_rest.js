(function(a) {
    'use strict';
    a.module('kao.rest', [])
        .controller('ListController', function ($scope, $http, navService) {
            $scope.records = [];
            $http.get(navService.getApiUrl()).success(function(data) {
                $scope.records = data.records;
            }).error(function(error) {
                console.log(error);
            });
        })
        .controller('NewController', function ($scope, $http, navService) {
            $scope.record = {};
            
            $scope.create = function() {
                $http.post(navService.getApiUrl(), $scope.record).success(function(data) {
                    
                }).error(function(error) {
                    console.log(error);
                });
            };
        });
})(angular);