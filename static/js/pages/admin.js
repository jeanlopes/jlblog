/*global require, document*/

require(['../lib/knockout',
         '../config/global',
         '../models/PostModel',
         '../viewModels/admin',
         '../common',
         '../lib/ckeditor/ckeditor',
         '../lib/jquery.min'], function (ko, g, PostModel, AdminViewModel, Common) {

    'use strict';
    var common = new Common();
    common.applyBindings(new AdminViewModel());
});