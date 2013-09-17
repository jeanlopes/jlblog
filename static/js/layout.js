/*global require, document, window, define*/

require(['./jquery.min'], function($) {
    window.console.log($); // OK
});

/**
var ko = require('./knockout-2.2.1.js');


$(document).ready(function() {    
    ko.applyBindings({accountViewModel: new window.accountViewModel(), postModel : new window.postModel(),  interestsListModel : new window.interestsListModel()  });
    
    $('#modalLogin').on('shown', function() {
        $("#user").focus();
    });
    
});


if (window.interestsListModel === undefined) {	
    window.interestsListModel = function() { };
}

if (window.postModel === undefined) {
    window.postModel = function() { };
}

*/