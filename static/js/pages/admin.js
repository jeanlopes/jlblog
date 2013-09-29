/*global require, document*/

require(['../lib/ckeditor/ckeditor',
         '../lib/jquery.min',
         '../lib/knockout',
         '../config/global',
         '../models/PostModel'], function (ko, g, PostModel) {

    setTimeout('window.CKEDITOR.replace(\'editor\')', 1000);
});