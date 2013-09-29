/**
 * Created by jean on 29/09/13.
 */

define(['../lib/knockout',
        '../lib/require-jquery'], function(ko, $) {

    'use strict';

    var PostModel = function () {

        var self = this;

        /*
        self.insertSyntax = function () {
            var t = $('table.k-editor iframe').contents().find('body');
            t.append(' &#60;pre class="brush: '+ $('#highlighter').val() +';"&#62;&#60;/pre&#62;');
            $('#highlighter').val('');
        };

        self.addSyntaxHighlighter = function () {

            $('ul.k-editor-toolbar')
                .parent()
                .append('<li style="list-style-type: none;" class="k-editor-select-box" data-bind="template: {name:\'syntaxHighlighterDropdown\'}"></li>');

        }

        */
    }

    return PostModel;

});