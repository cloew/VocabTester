(function(a) {
    'use strict';
    a.module('kao.rest', [])
        .provider('CrudConfig', function() {
            var crudConfigs = [];
            this.add = function(apiUrl, paths) {
                crudConfigs.push({apiUrl: apiUrl, paths: paths});
            };
            this.$get = function() {
                return crudConfigs;
            };
        })
        .factory('CrudWrapper', function($http) {
            function CrudWrapper(apiUrl) {
                this.apiUrl = apiUrl;
            };
            CrudWrapper.prototype.getAll = function() {
                return $http.get(this.apiUrl);
            };
            CrudWrapper.prototype.create = function(record) {
                return $http.post(this.apiUrl, record);
            };
            CrudWrapper.prototype.get = function(recordId) {
                return $http.get(this.apiUrl+'/'+recordId);
            };
            CrudWrapper.prototype.update = function(record) {
                return $http.put(this.apiUrl+'/'+record.id, record);
            };
            CrudWrapper.prototype.delete = function(recordId) {
                return $http.delete(this.apiUrl+'/'+recordId);
            };
            return CrudWrapper;
        })
        .factory('CrudWrappers', function($route, CrudWrapper, CrudConfig) {
            var pathToWrappers = {}
            var wrappers = {
                addCrud: function(apiUrl, paths) {
                    var wrapper = new CrudWrapper(apiUrl);
                    for (var i = 0; i < paths.length; i++) {
                        pathToWrappers[paths[i]] = wrapper;
                    }
                },
                getCurrentCrud: function() {
                    return pathToWrappers[$route.current.$$route.path];
                }
            };
            for (var i = 0; i < CrudConfig.length; i++) {
                wrappers.addCrud(CrudConfig[i].apiUrl, CrudConfig[i].paths);
            }
            return wrappers;
        })
        .controller('ListController', function ($scope, $location, CrudWrappers) {
            $scope.records = [];
            var crud = CrudWrappers.getCurrentCrud();
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.delete = function(id) {
                crud.delete(id).success(function(data) {
                    $scope.getRecords();
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.getRecords = function() {
                crud.getAll().success(function(data) {
                    $scope.records = data.records;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecords();
        })
        .controller('EditController', function ($scope, $location, $routeParams, CrudWrappers) {
            $scope.record = {};
            var crud = CrudWrappers.getCurrentCrud();
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.save = function() {
                crud.update($scope.record).success(function(data) {
                    $scope.record = data.record;
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.delete = function(id) {
                crud.delete($routeParams.id).success(function(data) {
                    $scope.goTo('/admin/languages');
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.getRecord = function() {
                crud.get($routeParams.id).success(function(data) {
                    $scope.record = data.record;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecord();
        })
        .controller('NewController', function ($scope, $location, CrudWrappers) {
            $scope.record = {};
            var crud = CrudWrappers.getCurrentCrud();
            
            $scope.save = function() {
                crud.create($scope.record).success(function(data) {
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