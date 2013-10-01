/*global require, window*/

require(['../lib/knockout', '../common'], function(ko, Common) {

    'use strict';
    var common = new Common();
    common.applyBindings();

    console.log(ko.dataFor(document.body));
});