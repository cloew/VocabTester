(function(a) {
    'use strict';
    a.module('kao.crud.api', [])
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
        });
})(angular);