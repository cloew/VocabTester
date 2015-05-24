(function(a) {
    'use strict';
    a.module('kao.crud.frontend', ['kao.crud.api', 'kao.utils', 'kao.loading'])
        .provider('FrontEndCrudConfig', function() {
            var crudConfigs = [];
            this.add = function(config) {
                crudConfigs.push(config);
            };
            this.$get = function() {
                return crudConfigs;
            };
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
                this.afterEditDirective = config.afterEditDirective;
            };
            CrudFrontEnd.prototype.getProperNestedConfig = function(varName) {
                var nested = this.nested;
                if (nested) {
                    if (nested[varName]) {
                        nested = {param: nested[varName], provider: nested.provider};
                    }
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
        .directive('kaoCrudList', function() {
          return {
            restrict: 'E',
            replace: true,
            templateUrl: 'static/partials/admin/kao_crud_list.html',
            scope: {
                type: '@'
            },
            controller: function ($scope, $location, CrudApiService, FrontEndCrudService, LoadingTrackerService) {
                var frontEndCrud;
                if ($scope.type) {
                    frontEndCrud = FrontEndCrudService.getFrontEndFor($scope.type);
                } else {
                    frontEndCrud = FrontEndCrudService.getCurrentCrud();
                }
                var crudApi = CrudApiService.getApiFor(frontEndCrud.name);
                var tracker =  LoadingTrackerService.get('list');
                
                $scope.records = [];
                $scope.dataType = frontEndCrud.name;
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
                    tracker.load(crudApi.getAll()).success(function(data) {
                        $scope.records = data.records;
                    }).error(function(error) {
                        console.log(error);
                    });
                };
                $scope.getRecords();
            }
        }})
        .directive('kaoCrudNew', function() {
          return {
            restrict: 'E',
            replace: true,
            templateUrl: 'static/partials/admin/kao_crud_new.html',
            scope: {
                type: '@'
            },
            controller: function ($scope, $location, CrudApiService, FrontEndCrudService) {
                var frontEndCrud;
                if ($scope.type) {
                    frontEndCrud = FrontEndCrudService.getFrontEndFor($scope.type);
                } else {
                    frontEndCrud = FrontEndCrudService.getCurrentCrud();
                }
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
            }
        }})
        .directive('kaoCrudEdit', function() {
          return {
            restrict: 'E',
            replace: true,
            templateUrl: 'static/partials/admin/kao_crud_edit.html',
            scope: {
                type: '@'
            },
            controller: function ($scope, $location, $routeParams, CrudApiService, FrontEndCrudService) {
                var frontEndCrud;
                if ($scope.type) {
                    frontEndCrud = FrontEndCrudService.getFrontEndFor($scope.type);
                } else {
                    frontEndCrud = FrontEndCrudService.getCurrentCrud();
                }
                var crudApi = CrudApiService.getApiFor(frontEndCrud.name);
                $scope.record = {};
                $scope.dataType = frontEndCrud.name;
                $scope.formDirective = frontEndCrud.formDirective;
                $scope.afterEditDirective = frontEndCrud.afterEditDirective;
                
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
            }
        }})
        .directive('listHeader', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/list_header.html'
            }
        })
        .directive('newHeader', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/new_header.html'
            }
        })
        .directive('editHeader', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/edit_header.html'
            }
        })
        .directive('modelTable', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/model_table.html'
            }
        })
        .directive('modelForm', function() {
            return {
                restrict: 'E',
                replace: true,
                templateUrl: 'static/partials/directives/admin/model_form.html'
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
        })
        .directive('kaoSelect', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                  model: '=',
                  url: '@',
                  displayField: '@'
                },
                controller: function($scope, $http) {
                    $scope.records = [];
                
                    $scope.getRecords = function() {
                        $http.get($scope.url).success(function(data) {
                            $scope.records = data.records;
                        }).error(function(error) {
                            console.log(error);
                        });
                    };
                    $scope.getRecords();
                },
                templateUrl: 'static/partials/directives/admin/model_select.html'
            }
        })
        .directive('modelSelect', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                  model: '=',
                  type: '@',
                  displayField: '@'
                },
                controller: function($scope, CrudApiService) {
                    var crudApi = CrudApiService.getApiFor($scope.type);
                    $scope.records = [];
                
                    $scope.getRecords = function() {
                        crudApi.getAll().success(function(data) {
                            $scope.records = data.records;
                        }).error(function(error) {
                            console.log(error);
                        });
                    };
                    $scope.getRecords();
                },
                templateUrl: 'static/partials/directives/admin/model_select.html'
            }
        });
})(angular);