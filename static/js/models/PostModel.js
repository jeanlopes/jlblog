/**
 * Created by jean on 29/09/13.
 */

define(['../lib/knockout'], function(ko) {

    'use strict';

    var PostModel = function () {

        var self = this;

        self.PUBLISHED = true;
        self.UNPUBLISHED = false;

        self.selected = false;
        self.id = 0;
        self.content = ko.observable("");
        self.state = self.UNPUBLISHED;
        self.date = new Date();
        self.author = "";

        self.getTitle = function()
        {
            // pesquisar no content sobre o title com xpath...
        }

    };

    return PostModel;

});