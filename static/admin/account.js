
$("#birth").kendoDatePicker();

$('#interests')[0].setCustomValidity('Adicione um item na lista');

var interestsListModel = function () {
    this.itemToAdd = ko.observable("");
    this.allItems = ko.observableArray([]); 
    this.selectedItems = ko.observableArray([]); 
 	
    this.addItem = function () {
        if ((this.itemToAdd() != "") && (this.allItems.indexOf(this.itemToAdd()) < 0)) // Prevent blanks and duplicates
            this.allItems.push(this.itemToAdd());
        this.itemToAdd(""); // Clear the text box
    };
 
    this.removeSelected = function () {
        this.allItems.removeAll(this.selectedItems());
        this.selectedItems([]); // Clear selection
    };
 
};