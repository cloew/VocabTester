(function(a) {
    "use strict";
    a.module('Forms', ['kao.utils', 'kao.loading', 'VocabNav', 'Language'])
        .factory('Form', function(LanguageService, KaoDefer) {
            function Form(config) {
                this.config = config;
                this.name = config.name;
                this.pluralName = config.pluralName;
                this.isWords = config.isWords;
                this.randomQuizPath = config.randomQuizPath;
            };
            Form.prototype.getLearned = function() {
                var deferred = KaoDefer();
                var self = this;
                LanguageService.withCurrentLanguage(function(language) {
                    self.config.getLearned(language).success(deferred.resolve).error(deferred.reject);
                });
                return deferred.promise;
            };
            Form.prototype.getLists = function() {
                var deferred = KaoDefer();
                var self = this;
                LanguageService.withCurrentLanguage(function(language) {
                    self.config.getLists(language).success(deferred.resolve).error(deferred.reject);
                });
                return deferred.promise;
            };
            Form.prototype.getQuizUrl = function(id) {
                return this.config.quizPath.replace(':listId', id);
            };
            return Form;
        })
        .factory('Word', function(Form, navService) {
            var config = {name: "Word",
                          pluralName: "Words",
                          isWords: true,
                          quizPath: navService.wordListQuiz.path,
                          randomQuizPath: navService.randomWordQuiz.path,
                          getLearned: function(language) {
                            return language.getWords();
                            },
                          getLists: function(language) {
                            return language.getWordLists();
                            }
                         };
            return new Form(config);
        })
        .factory('Symbol', function(Form, navService) {
            var config = {name: "Symbol",
                          pluralName: "Symbols",
                          isWords: false,
                          quizPath: navService.symbolListQuiz.path,
                          randomQuizPath: navService.randomSymbolQuiz.path,
                          getLearned: function(language) {
                            return language.getSymbols();
                            },
                          getLists: function(language) {
                            return language.getSymbolLists();
                            }
                         };
            return new Form(config);
        })
        .service('FormsService', function($route, navService, Symbol, Word) {
            var service = {current: function() {
                return this[$route.current.$$route.path];
            }};
            service[navService.words.path] = Word;
            service[navService.wordLists.path] = Word;
            service[navService.symbols.path] = Symbol;
            service[navService.symbolLists.path] = Symbol;
            return service;
        })
        .directive('formLists', function() {
            return {
                restrict: 'E',
                replace: true,
                controller: function($scope, FormsService, LanguageService, LoadingTrackerService) {
                    var form = FormsService.current();
                    $scope.formName = form.name;
                    var tracker = LoadingTrackerService.get('forms');
                    
                    LanguageService.watchCurrentLanguage($scope, function(event, language) {
                        tracker.load(form.getLists()).success(function(data) {
                            $scope.lists = data.lists;
                        }).error(function(error) {
                            console.log(error);
                        });
                    });
                },
                templateUrl: 'static/partials/directives/form_lists.html'
            }
        })
        .directive('formList', function() {
            return {
                restrict: 'E',
                replace: true,
                scope: {
                    conceptList: '='
                },
                controller: function($scope, FormsService) {
                    var form = FormsService.current();
                    $scope.header = form.pluralName.toLowerCase();
                    $scope.isWords = form.isWords;
                    $scope.quizUrl = form.getQuizUrl($scope.conceptList.id);
                },
                templateUrl: 'static/partials/directives/concept_list.html'
            }
        });
})(angular);