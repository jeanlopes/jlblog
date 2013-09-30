/**
 * Created by jean on 29/09/13.
 */

define(['../lib/knockout',
        '../lib/require-jquery'], function(ko, $) {

    'use strict';

    var PostModel = function () {

        var self = this;

        self.PUBLISHED = 1;
        self.UNPUBLISHED = 2;
        self.DISCARTED = 3;

        self.Id = 0;
        self.Content = ko.observable("");
        self.State = self.UNPUBLISHED;
        self.Date = new Date();

    };

    return PostModel;

});