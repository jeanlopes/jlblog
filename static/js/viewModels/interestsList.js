/*global define*/
define(['../lib/require-jquery','../lib/knockout', '../config/global', '../models/InterestsListModel'], function($, ko, g, InterestsList) {

	
	var InterestsListViewModel = function() {
		
		
		var self = this;
		
		var interestsList = [];
		$('input[name="interestsList[]"]').each(function(index) {
			self.interestsList.push($($('input[name="interestsList[]"]')[index]).val());
		});

		/**
		 * @property lista com todos os itens adicionados
		 */
		this.allItems = ko.observableArray(interestsList);
		
		
		/**
		 * @property lista com os itens selecionados 
		 */
		this.selectedItems = ko.observableArray(interestsList);

		/**
		 * @function adiciona um novo item na lista
		 */
		this.addItem = function() {
			if ((this.itemToAdd() !=="") && (this.allItems.indexOf(this.itemToAdd()) < 0))// Prevent blanks and duplicates
			{
				this.allItems.push(this.itemToAdd());
				this.selectedItems.push(this.itemToAdd());
			}
			this.itemToAdd("");
			// Clear the text box
		};

		/**
		 * @function remove um item selecionado
		 */
		this.removeSelected = function() {
			this.allItems.removeAll(this.selectedItems());
			this.selectedItems([]);
			// Clear selection
		};
	};
	
	return InterestsListViewModel;
});
