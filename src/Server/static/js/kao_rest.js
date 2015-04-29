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
            this.add = function(apiUrl, dataType, nested) {
                crudConfigs.push({apiUrl: apiUrl, dataType: dataType, nested: nested});
            };
            this.$get = function() {
                return crudConfigs;
            };
        })
        .provider('FrontEndCrudConfig', function() {
            var crudConfigs = [];
            this.add = function(config) {
                crudConfigs.push(config);
            };
            this.$get = function() {
                return crudConfigs;
            };
        })
        .factory('NestedRouteService', function($injector) {
            this.getUrl = function(apiUrl, nested) {
                var apiUrl = apiUrl;
                if (nested) {
                    for (var i = 0; i < nested.length; i++) {
                        apiUrl = apiUrl.replace(':'+nested[i].param, nested[i].provider.get($injector))
                    }
                }
                return apiUrl;
            }
            return this;
        })
        .factory('CrudApi', function($http, NestedRouteService) {
            function CrudApi(apiUrl, nested) {
                this.apiUrl = apiUrl;
                this.nested = nested;
            };
            CrudApi.prototype.getBaseUrl = function() {
                return NestedRouteService.getUrl(this.apiUrl, this.nested);
            };
            CrudApi.prototype.getAll = function() {
                return $http.get(this.getBaseUrl());
            };
            CrudApi.prototype.create = function(record) {
                return $http.post(this.getBaseUrl(), record);
            };
            CrudApi.prototype.get = function(recordId) {
                return $http.get(this.getBaseUrl()+'/'+recordId);
            };
            CrudApi.prototype.update = function(record) {
                return $http.put(this.getBaseUrl()+'/'+record.id, record);
            };
            CrudApi.prototype.delete = function(recordId) {
                return $http.delete(this.getBaseUrl()+'/'+recordId);
            };
            return CrudApi;
        })
        .factory('CrudApiService', function($route, CrudApi, CrudApiConfig) {
            var dataTypeToApi = {}
            var service = {
                addCrud: function(apiUrl, dataType, nested) {
                    dataTypeToApi[dataType] = new CrudApi(apiUrl, nested);
                },
                getApiFor: function(dataType) {
                    return dataTypeToApi[dataType];
                }
            };
            for (var i = 0; i < CrudApiConfig.length; i++) {
                service.addCrud(CrudApiConfig[i].apiUrl, CrudApiConfig[i].dataType, CrudApiConfig[i].nested);
            }
            return service;
        })
        .factory('FrontEndCrud', function(NestedRouteService) {
            function CrudFrontEnd(config) {
                this.name = config.name;
                this.pluralName = config.pluralName;
                if (!this.pluralName && this.name) {
                    this.pluralName = this.name + 's';
                }
                this.nested = config.nested;
                this.primaryPaths = config.primaryPaths;
                this.listUrl = config.listUrl;
                this.newUrl = config.newUrl;
                this.editUrl = config.editUrl;
                
                this.tableDirective = config.tableDirective;
                this.formDirective = config.formDirective;
            };
            CrudFrontEnd.prototype.getProperNestedConfig = function(varName) {
                var nested = this.nested;
                if (nested[varName]) {
                    nested = {param: nested[varName], provider: nested.provider};
                }
                return nested;
            };
            CrudFrontEnd.prototype.getListUrl = function() {
                return NestedRouteService.getUrl(this.listUrl, this.getProperNestedConfig('list'));
            };
            CrudFrontEnd.prototype.getNewUrl = function() {
                return NestedRouteService.getUrl(this.newUrl, this.getProperNestedConfig('new'));
            };
            CrudFrontEnd.prototype.getEditUrl = function(id) {
                return NestedRouteService.getUrl(this.editUrl, this.getProperNestedConfig('edit')).replace(':id', id);
            };
            return CrudFrontEnd;
        })
        .factory('FrontEndCrudService', function($route, FrontEndCrud, FrontEndCrudConfig) {
            var dataTypeToWrapper = {}
            var pathToWrappers = {}
            var service = {
                addCrud: function(config) {
                    dataTypeToWrapper[config.name] = config;
                    var paths;
                    if (config.primaryPaths) {
                        paths = config.primaryPaths;
                    } else {
                        paths = [config.listUrl, config.newUrl, config.editUrl];
                    }
                    for (var i = 0; i < paths.length; i++) {
                        if (paths[i]) {
                            pathToWrappers[paths[i]] = config;
                        }
                    }
                },
                getCurrentCrud: function() {
                    return pathToWrappers[$route.current.$$route.path];
                },
                getFrontEndFor: function(dataType) {
                    return dataTypeToWrapper[dataType];
                }
            };
            for (var i = 0; i < FrontEndCrudConfig.length; i++) {
                service.addCrud( new FrontEndCrud(FrontEndCrudConfig[i]));
            }
            return service;
        })
        .controller('ListController', function ($scope, $location, CrudApiService, FrontEndCrudService) {
            var frontEndCrud = FrontEndCrudService.getCurrentCrud();
            var crudApi = CrudApiService.getApiFor(frontEndCrud.name);
            $scope.records = [];
            $scope.dataType = frontEndCrud.pluralName;
            $scope.pluralDataType = frontEndCrud.pluralName;
            $scope.newUrl = '#'+frontEndCrud.getNewUrl();
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
                    $scope.goTo(frontEndCrud.getListUrl());
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