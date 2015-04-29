(function(a) {
    'use strict';
    a.module('kao.rest', [])
        .provider('CrudParamFromRouteConfig', function() {
            var paramToConfig = {};
            var CrudParamFromRoute = function(pathConfigs) {
                this.pathConfigs = {};
                for (var i = 0; i < pathConfigs.length; i++) {
                    this.pathConfigs[pathConfigs[i].path] = pathConfigs[i].param;
                }
            };
            CrudParamFromRoute.prototype.get = function($injector) {
                return $injector.invoke(function($route, $routeParams) {
                    return $routeParams[this.pathConfigs[$route.current.$$route.path]];
                }, this);
            };
            
            this.register = function(param, pathConfigs) {
                paramToConfig[param] = new CrudParamFromRoute(pathConfigs);
            };
            this.forParam = function(param) {
                return paramToConfig[param];
            };
            this.$get = function() {
                return this;
            };
        })
        .provider('CrudApiConfig', function() {
            var crudConfigs = [];
            this.add = function(apiUrl, dataType) {
                crudConfigs.push({apiUrl: apiUrl, dataType: dataType});
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
            var dataTypeToApi = {}
            var service = {
                addCrud: function(apiUrl, dataType) {
                    dataTypeToApi[dataType] = new CrudApi(apiUrl);
                },
                getApiFor: function(dataType) {
                    return dataTypeToApi[dataType];
                }
            };
            for (var i = 0; i < CrudApiConfig.length; i++) {
                service.addCrud(CrudApiConfig[i].apiUrl, CrudApiConfig[i].dataType);
            }
            return service;
        })
        .factory('FrontEndCrudService', function($route, FrontEndCrudConfig) {
            var pathToWrappers = {}
            var service = {
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
                service.addCrud(FrontEndCrudConfig[i]);
            }
            return service;
        })
        .controller('ListController', function ($scope, $location, CrudApiService, FrontEndCrudService) {
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            var crudApi = CrudApiService.getApiFor(frontEndCrud.name);
            $scope.records = [];
            $scope.dataType = frontEndCrud.pluralName;
            $scope.pluralDataType = frontEndCrud.pluralName;
            $scope.newUrl = '#'+frontEndCrud.newUrl;
            $scope.tableDirective = frontEndCrud.tableDirective;
            
            $scope.goTo = function(path) {
                $location.path(path);
            };
            
            $scope.getRecordEditUrl = function(record) {
                return '#'+frontEndCrud.getEditUrl(record.id);
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
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            var crudApi = CrudApiService.getApiFor(frontEndCrud.name);
            $scope.record = {};
            $scope.dataType = frontEndCrud.name;
            $scope.formDirective = frontEndCrud.formDirective;
            
            $scope.save = function() {
                crudApi.create($scope.record).success(function(data) {
                    $location.path(frontEndCrud.getEditUrl(data.record.id));
                }).error(function(error) {
                    console.log(error);
                });
            };
        })
        .controller('EditController', function ($scope, $location, $routeParams, CrudApiService, FrontEndCrudService) {
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            var crudApi = CrudApiService.getApiFor(frontEndCrud.name);
            $scope.record = {};
            $scope.dataType = frontEndCrud.name;
            $scope.formDirective = frontEndCrud.formDirective;
            
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
        .directive('kaoRestTable', function($compile) {
            return {
                restrict: 'E',
                replace: true,
                link: function(scope, element, attrs) {
                    var dom = '<'+attrs.tableDirective+'>'+'</'+attrs.tableDirective+'>'
                    var el = $compile(dom)(scope);
                    element.append(el);
                }
            }
        })
        .directive('kaoRestForm', function($compile) {
            return {
                restrict: 'E',
                replace: true,
                link: function(scope, element, attrs) {
                    var dom = '<'+attrs.formDirective+'>'+'</'+attrs.formDirective+'>'
                    var el = $compile(dom)(scope);
                    element.append(el);
                }
            }
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