'use strict';

var services = angular.module('VocabTesterServices', ['VocabNavServices']);

services.factory('conceptTableService', function() {
    return {
        buildEntries: function (concepts, isWords) {
            var columns = [];
            
            if (isWords) {
                columns.push({'name':'Word', 'path':'form'});
            }
            else {
                columns.push({'name':'Symbol', 'path':'form'});
            }
            columns.push({'name':'Native', 'path':'native'});
            columns.push({'name':'Mastery', 'path':'mastery'});
            
            var table = {'entries':[], columns:columns};
            for (var i = 0; i < concepts.length; i++) {
                table.entries.push({'form':concepts[i].foreign.text, 'native':concepts[i].native.text, 'mastery':concepts[i].foreign.mastery});
            }
            return table;
        }
    };
});

services.factory('quizResultsTableService', function(conceptTableService) {
    return {
        buildEntries: function (quiz) {
            var concepts = [];
            for (var i = 0; i < quiz.quiz.questions.length; i++) {
                var question = quiz.quiz.questions[i];
                concepts.push(question.subject);
            }
            var table = conceptTableService.buildEntries(concepts, quiz.isWords);
            for (var i = 0; i < quiz.quiz.questions.length; i++) {
                var question = quiz.quiz.questions[i];
                if (question.results.correct) {
                    table.entries[i].rowClass = 'success';
                }
                else {
                    table.entries[i].rowClass = 'danger';
                }
            }
            return table;
        }
    };
});

services.factory('quizService', function($http, $location, $routeParams, navService) {
    function Quiz(wordListId) {
        this.wordListId = wordListId;
        this.quiz = undefined;
        this.currentQuestionIndex = 0;
        this.correctAnswers = 0;
        this.returnTo = navService.getReturnTo();
        
        var self = this;
        $http.get('/api' +$location.path()).success(function(data) {
            self.quiz = data.quiz;
            self.currentQuestion =  self.quiz.questions[self.currentQuestionIndex];
            self.numberOfQuestions = self.quiz.questions.length;
        }).error(function(error) {
            console.log(error);
        });
    };
    
    Quiz.prototype.answer = function() {
        var question = this.currentQuestion;
        var self = this;
        if (question.selectedIndex !== undefined) {
            var correct = question.selectedIndex == this.currentQuestion.answerIndex;
            self.grading = true;
            $http.post(question.answerUrl, {'correct':correct}).success(function(data) {
                question.results = {"correct":correct};
                if (correct) {
                    self.correctAnswers += 1;
                }
                question.subject.foreign.mastery = data.rating;
                self.grading = false;
            }).error(function(error) {
                console.log(error);
            });
        }
    };
    
    Quiz.prototype.next = function() {
        this.currentQuestionIndex = this.currentQuestionIndex+1;
        this.currentQuestion =  this.quiz.questions[this.currentQuestionIndex];
        this.completed = (this.currentQuestionIndex == this.quiz.questions.length);
    };
    
    Quiz.prototype.canSubmit = function() {
        return this.currentQuestion && (this.currentQuestion.selectedIndex >= 0) && !this.grading;
    };
    
    return {
        buildQuiz: function () {
            return new Quiz($routeParams.listId);
        }
    };
});

services.factory('userService', function($http, $window, $route) {
    var user = undefined;
    var userWatch = [];
    var responseHandler = function(promise, successCallback, errorCallback) {
        promise.success(function(data) {
            if (data.error) {
                errorCallback(data.error);
            } else {
                user = data.user;
                $window.sessionStorage.token = data.token;
                successCallback();
                for (var i = 0; i < userWatch.length; i++) {
                    userWatch[i](user);
                }
            }
        }).error(function(error) {
            console.log(error);
        });
    }

    return {
        login: function (email, password, successCallback, errorCallback) {
            responseHandler($http.post('/api/login', {'email':email, 'password':password}), successCallback, errorCallback);
        },
        register: function (params, successCallback, errorCallback) {
            responseHandler($http.post('/api/register', {'email':params.email, 'password':params.password, 'givenName':params.firstName, 'lastName':params.lastName}), successCallback, errorCallback);
        },
        logout: function () {
            delete $window.sessionStorage.token;
            user = undefined;
            $route.reload();
        },
        isLoggedIn: function () {
            return $window.sessionStorage.token !== undefined
        },
        watchUser: function(callback) {
            userWatch.push(callback);
            if (this.isLoggedIn()) {
                if (user === undefined) {
                    $http.get('/api/users/current').success(function(data) {
                        user = data.user;
                        callback(user);
                    }).error(function(error) {
                        console.log(error);
                    });
                } else  {
                    callback(user);
                }
            }
        }
    };
});
services.factory('authInterceptor', function ($rootScope, $q, $window, $location) {
  return {
    request: function (config) {
      config.headers = config.headers || {};
      if ($window.sessionStorage.token) {
        config.headers.Authorization = 'Bearer ' + $window.sessionStorage.token;
      }
      return config;
    },
    responseError: function (rejection) {
      if (rejection.status === 401) {
        var returnToPath = $location.path();
        $location.path('/login').search('returnTo', returnToPath);
      }
      return $q.reject(rejection);
    }
  };
});

services.config(function ($httpProvider) {
  $httpProvider.interceptors.push('authInterceptor');
});