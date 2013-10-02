/**
 * Created by jean on 30/09/13.
 */

define(['../lib/require-jquery',
        '../lib/knockout',
        '../config/global'], function($, ko, g) {

    'use strict';

    var AdminViewModel = function (posts) {

        var self = this;

        self.defaultPostsAmount = 50;
        self.posts = ko.observableArray(posts | []);
        self.searchResults = ko.observableArray([]);
        self.hasSearch = ko.observable(false);

        self.search = ko.computed({
				read: function() {
                    console.log('está lendo os valores');
				},
				// seta todos para completados / não completados
				write: function(newValue) {
                    console.log('está escrevendo os valores');
				}
		    });

        self.create = function()
        {

            $.post(g.createPostURI, null, null, "json")
                .done(function (post)
                {
                    self.posts.push(post);
                    self.openEditing(post);
                });

        };

        self.publish = function(postId)
        {
            ko.utils.arrayForEach(self.posts(), function(post) {
			    // seta mesmo se o valor é o mesmo
				if (post.id == postId) {
                    post.state = post.PUBLISHED;
                    $.post(g.publishPostURI,
                           postId,
                           alert('post ' + postId + ' publicado!'),
                           "json");
                 }
			});
        };

        self.unpublish = function(postId)
        {
            ko.utils.arrayForEach(self.posts(), function(post) {
						// seta mesmo se o valor é o mesmo
                if (post.id != postId) {
                    post.state = post.UNPUBLISHED;
                    $.post(g.unpublishPostURI,
                           postId,
                           alert('post ' + postId + ' despublicado!'),
                           "json");
                }
			});
        };

        self.discart = function(post)
        {
            $.ajax({ type: "DELETE", url: g.deletePostURI + '/' + post.Id })
                .done(function ()
                {
                    self.posts.remove(post);
                    self.closeEditing();
                });
        };

        // salvar (a cada 5s depois do último evento)
        self.save = function(post)
        {
            $.ajax({ type: "PUT", url: g.savePostURI + '/' + post.id, data: post });
        };

        self.closePost = function(post)
        {
            self.save(post);
            self.closeEditing();
        };

        self.openPost = function(post)
        {
            self.openEditing(post);
            setTimeout('window.CKEDITOR.replace(\'editor\')', 1000);
            self.editor(post.content);
        };

        self.listPosts = function(amount)
        {
            $.getJSON(g.listPostsURI + "/" + amount, self.posts);
        };

        self.checkAll = ko.computed({
				// seta todos para completados / não completados
				write: function(newValue) {
					ko.utils.arrayForEach(self.posts(), function(post) {
						// seta mesmo se o valor é o mesmo
						post.state = newValue;
					});
				}
		    });

        self.openEditing = function(post)
        {
            self.creatingButtonEnabled(false);
            self.discartingButtonEnabled(true);

            if (post.state == post.PUBLISHED)
            {
                self.publishingButtonVisible(false);
                self.unpublishingButtonVisible(true);
            }
            else
            {
                self.publishingButtonVisible(true);
                self.unpublishingButtonVisible(false);
            }

            self.closingButtonVisible(true);
            self.deleteButtonVisible(false);
        }

        self.closeEditing = function ()
        {
            self.creatingButtonEnabled(true);
            self.discartingButtonEnabled(false);
            self.deleteButtonVisible(true);
            self.delteButtonEnabled(false);
            self.publishingButtonVisible(true);
            self.publishingButtonEnabled(false);
            self.closingButtonVisible(false);
            self.unpublishingButtonVisible(true);
        }

        self.creatingButtonEnabled = ko.observable(false);
        self.discartingButtonEnabled = ko.observable(false);
        self.publishingButtonVisible = ko.observable(false);
        self.publishingButtonEnabled = ko.observable(false);
        self.unpublishingButtonVisible = ko.observable(false);
        self.closingButtonVisible = ko.observable(false);
        self.deleteButtonVisible = ko.observable(false);
        self.delteButtonEnabled = ko.observable(false);

        self.editor = ko.observable("");
        self.showEditor = ko.observable(false);
        self.closeEditing();
        self.listPosts(self.defaultPostsAmount);
    };

    return AdminViewModel;

});