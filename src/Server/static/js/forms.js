(function(a) {
    "use strict";
    a.module('Forms', ['VocabNav', 'Language'])
        .factory('KaoPromise', function($q) {
            function KaoPromise() {
                var defer = $q.defer();
                defer.promise.success = function(fn) {
                    defer.promise.then(function() {
                        fn.apply(this, arguments)
                    });
                    return defer.promise;
                };

                defer.promise.error = function(fn) {
                    defer.promise.then(null, function() {
                        fn.apply(this, arguments);
                    });
                    return defer.promise;
                };

                return defer;
            };
            return KaoPromise;
        })
        .factory('Form', function(LanguageService, KaoPromise) {
            function Form(config) {
                this.config = config;
                this.name = config.name;
                this.randomQuizPath = config.randomQuizPath;
            };
            Form.prototype.getLearned = function() {
                var deferred = KaoPromise();
                var self = this;
                LanguageService.withCurrentLanguage(function(language) {
                    self.config.getLearned(language).success(deferred.resolve).error(deferred.reject);
                });
                return deferred.promise;
            };
            return Form;
        })
        .factory('Word', function(Form, navService) {
            var config = {name: "Words",
                          randomQuizPath: navService.randomWordQuiz.path, 
                          getLearned: function(language) {
                            return language.getWords();
                            }
                         };
            return new Form(config);
        })
        .factory('Symbol', function(Form, navService) {
            var config = {name: "Symbols",
                          randomQuizPath: navService.randomSymbolQuiz.path,
                          getLearned: function(language) {
                            return language.getSymbols();
                            }
                         };
            return new Form(config);
        })
        .service('FormsService', function($route, navService, Symbol, Word) {
            var service = {current: function() {
                return this[$route.current.$$route.path];
            }};
            service[navService.words.path] = Word;
            service[navService.symbols.path] = Symbol;
            return service;
        });
})(angular);