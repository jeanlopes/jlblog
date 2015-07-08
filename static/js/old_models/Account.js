/*global define */
define(['../lib/knockout'], function(ko) {

    'use strict';
    var AccountModel = function(user, password) {

        this.user = ko.observable(user);
        this.password = ko.observable(password);

    };

    return AccountModel;
});