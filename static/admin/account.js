//$("#birth").kendoDatePicker();

//$('#interests')[0].setCustomValidity('Adicione um item na lista');

// pattern ='^(((((0[1-9])|(1\d)|(2[0-8]))\/((0[1-9])|(1[0-2])))|((31\/((0[13578])|(1[02])))|((29|30)\/((0[1,3-9])|(1[0-2])))))\/((20[0-9][0-9])|(19[0-9][0-9])))|((29\/02\/(19|20)(([02468][048])|([13579][26]))))$'

var interestsListModel = function() {

	this.interestsList = []
	var self = this;
	$('input[name="interestsList[]"]').each(function(index) {
		self.interestsList.push($($('input[name="interestsList[]"]')[index]).val());
	});

	this.itemToAdd = ko.observable("");
	this.allItems = ko.observableArray(this.interestsList);
	this.selectedItems = ko.observableArray(this.interestsList);

	this.addItem = function() {
		if ((this.itemToAdd() != "") && (this.allItems.indexOf(this.itemToAdd()) < 0))// Prevent blanks and duplicates
		{
			this.allItems.push(this.itemToAdd());
			this.selectedItems.push(this.itemToAdd());
		}
		this.itemToAdd("");
		// Clear the text box
	};

	this.removeSelected = function() {
		this.allItems.removeAll(this.selectedItems());
		this.selectedItems([]);
		// Clear selection
	};

};

