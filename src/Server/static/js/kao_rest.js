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
        .controller('EditController', function ($scope, $http, $location, navService) {
            $scope.record = {};
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.save = function(id) {
                $http.put(navService.getApiUrl(), $scope.record).success(function(data) {
                    $scope.record = data.record;
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.delete = function(id) {
                $http.delete(navService.getApiUrl()).success(function(data) {
                    $scope.goTo('/admin/languages');
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.getRecord = function() {
                $http.get(navService.getApiUrl()).success(function(data) {
                    $scope.record = data.record;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecord();
        })
        .controller('NewController', function ($scope, $http, $location, navService) {
            $scope.record = {};
            
            $scope.save = function() {
                $http.post(navService.getApiUrl(), $scope.record).success(function(data) {
                    $location.path('/admin/languages/' + data.record.id);
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