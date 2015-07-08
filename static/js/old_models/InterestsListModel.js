/*global define*/
define(['../lib/knockout'], function(ko) {

	'use strict';

	var interestsListModel = function() {

		// itemToAdd
		this.item = ko.observable("");

	};
	
	return interestsListModel;

}); 