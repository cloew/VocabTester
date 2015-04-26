(function(a) {
    'use strict';
    a.module('vocab.rest', ['kao.rest', 'VocabNav'])
        .config(['CrudConfigProvider', 'navConfigProvider',
            function(CrudConfig, navConfig) {
                var config = navConfig.config;
                CrudConfig.add('/api/admin/languages', [config.adminLanguages.path, config.adminNewLanguages.path, config.adminEditLanguages.path]);
            }
        ]);
})(angular);