/**
 * Created by jean on 30/09/13.
 */

define(['../lib/require-jquery',
        '../lib/knockout',
        '../config/global'], function($, ko, g) {

    'use strict';

    var AdminViewModel = function (posts) {

        var self = this;
        self.listPosts();

        self.posts = ko.observableArray(posts | []);

        self.create = function()
        {
            $.post(g.createPostURI, null, null, "json")
                .done(function (o) { self.posts.push(o); });
        };

        self.publish = function()
        {

        };

        self.unpublish = function()
        {

        };

        self.discart = function(post)
        {
            $.ajax({ type: "DELETE", url: g.deletePostURI + '/' + post.Id })
                .done(function () { self.posts.remove(post); });
        };

        // salvar (a cada 5s depois do último evento)
        self.save = function(post)
        {
            $.ajax({ type: "PUT", url: g.savePostURI + '/' + post.Id, data: post });
        };

        self.closePost = function()
        {

        };

        self.openPost = function(postId)
        {

        };

        self.listPosts = function()
        {
            $.getJSON(g.listPostsURI, self.posts);
        };
    };

    return AdminViewModel;

});