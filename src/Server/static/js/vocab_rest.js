(function(a) {
    'use strict';
    a.module('vocab.rest', ['kao.rest', 'VocabNav'])
        .config(['CrudConfigProvider', 'navConfigProvider',
            function(CrudConfig, navConfig) {
                CrudConfig.add('/api/admin/languages', [navConfig.adminLanguages.path, navConfig.adminNewLanguages.path, navConfig.adminEditLanguages.path]);
            }
        ]);
})(angular);