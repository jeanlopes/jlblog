/*global require*/
require(['./lib/knockout',
		 './config/global',
		 './extends/handlers',
		 './lib/knockout-amd-helpers',
		 './lib/require-jquery',
		 './lib/jquery.cookie',
		 './viewModels/account', './models/Account'], function(ko, g, $, AccountViewModel, Account ) {
	
	'use strict';
	
	// TODO: trabalhar no lembrar-me quando for guardar pra valer o nome de usuário
	//var todos = ko.utils.parseJson(window.localStorage.getItem(g.localStorageItem));
	var account = new Account($.cookie('auth'), '');
	ko.applyBindings(new AccountViewModel(account));
});