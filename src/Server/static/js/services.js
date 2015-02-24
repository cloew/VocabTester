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