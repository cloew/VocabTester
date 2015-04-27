(function(a) {
    'use strict';
    a.module('kao.rest', [])
        .provider('CrudApiConfig', function() {
            var crudConfigs = [];
            this.add = function(apiUrl, paths) {
                crudConfigs.push({apiUrl: apiUrl, paths: paths});
            };
            this.$get = function() {
                return crudConfigs;
            };
        })
        .provider('FrontEndCrudConfig', function() {
            var crudConfigs = [];
            function CrudFrontEnd(config) {
                this.name = config.name;
                this.pluralName = config.pluralName;
                if (!this.pluralName && this.name) {
                    this.pluralName = this.name + 's';
                }
                this.listUrl = config.listUrl;
                this.newUrl = config.newUrl;
                this.editUrl = config.editUrl;
                
                this.tableDirective = config.tableDirective;
                this.formDirective = config.formDirective;
            };
            CrudFrontEnd.prototype.getEditUrl = function(id) {
                return this.editUrl.replace(':id', id);
            };
            this.add = function(config) {
                crudConfigs.push(new CrudFrontEnd(config));
            };
            this.$get = function() {
                return crudConfigs;
            };
        })
        .factory('CrudApi', function($http) {
            function CrudApi(apiUrl) {
                this.apiUrl = apiUrl;
            };
            CrudApi.prototype.getAll = function() {
                return $http.get(this.apiUrl);
            };
            CrudApi.prototype.create = function(record) {
                return $http.post(this.apiUrl, record);
            };
            CrudApi.prototype.get = function(recordId) {
                return $http.get(this.apiUrl+'/'+recordId);
            };
            CrudApi.prototype.update = function(record) {
                return $http.put(this.apiUrl+'/'+record.id, record);
            };
            CrudApi.prototype.delete = function(recordId) {
                return $http.delete(this.apiUrl+'/'+recordId);
            };
            return CrudApi;
        })
        .factory('CrudApiService', function($route, CrudApi, CrudApiConfig) {
            var pathToWrappers = {}
            var wrappers = {
                addCrud: function(apiUrl, paths) {
                    var wrapper = new CrudApi(apiUrl);
                    for (var i = 0; i < paths.length; i++) {
                        pathToWrappers[paths[i]] = wrapper;
                    }
                },
                getCurrentCrud: function() {
                    return pathToWrappers[$route.current.$$route.path];
                }
            };
            for (var i = 0; i < CrudApiConfig.length; i++) {
                wrappers.addCrud(CrudApiConfig[i].apiUrl, CrudApiConfig[i].paths);
            }
            return wrappers;
        })
        .factory('FrontEndCrudService', function($route, FrontEndCrudConfig) {
            var pathToWrappers = {}
            var wrappers = {
                addCrud: function(config) {
                    var paths = [config.listUrl, config.newUrl, config.editUrl];
                    for (var i = 0; i < paths.length; i++) {
                        if (paths[i]) {
                            pathToWrappers[paths[i]] = config;
                        }
                    }
                },
                getCurrentCrud: function() {
                    return pathToWrappers[$route.current.$$route.path];
                }
            };
            for (var i = 0; i < FrontEndCrudConfig.length; i++) {
                wrappers.addCrud(FrontEndCrudConfig[i]);
            }
            return wrappers;
        })
        .controller('ListController', function ($scope, $location, CrudApiService, FrontEndCrudService) {
            var crudApi = CrudApiService.getCurrentCrud();
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            $scope.records = [];
            $scope.dataType = frontEndCrud.pluralName;
            $scope.newUrl = '#'+frontEndCrud.newUrl;
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.delete = function(id) {
                crudApi.delete(id).success(function(data) {
                    $scope.getRecords();
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.getRecords = function() {
                crudApi.getAll().success(function(data) {
                    $scope.records = data.records;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecords();
        })
        .controller('NewController', function ($scope, $location, CrudApiService, FrontEndCrudService) {
            var crudApi = CrudApiService.getCurrentCrud();
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            $scope.record = {};
            $scope.dataType = frontEndCrud.name;
            
            $scope.save = function() {
                crudApi.create($scope.record).success(function(data) {
                    $location.path(frontEndCrud.getEditUrl(data.record.id));
                }).error(function(error) {
                    console.log(error);
                });
            };
        })
        .controller('EditController', function ($scope, $location, $routeParams, CrudApiService, FrontEndCrudService) {
            var crudApi = CrudApiService.getCurrentCrud();
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            $scope.record = {};
            $scope.dataType = frontEndCrud.name;
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.save = function() {
                crudApi.update($scope.record).success(function(data) {
                    $scope.record = data.record;
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.delete = function(id) {
                crudApi.delete($routeParams.id).success(function(data) {
                    $scope.goTo(frontEndCrud.listUrl);
                }).error(function(error) {
                    console.log(error);
                });
            };
            
            $scope.getRecord = function() {
                crudApi.get($routeParams.id).success(function(data) {
                    $scope.record = data.record;
                }).error(function(error) {
                    console.log(error);
                });
            };
            $scope.getRecord();
        })
        .directive('toNewPage', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                  newUrl: '@'
                },
                templateUrl: 'static/partials/directives/admin/to_new_page.html'
            }
        })
        .directive('deleteButton', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                  deleteMethod: '=',
                  id: '=',
                  dataType: '@',
                },
                templateUrl: 'static/partials/directives/admin/delete_button.html'
            }
        })
        .directive('saveButton', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/save_button.html'
            }
        });
})(angular);