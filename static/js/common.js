/*global require, console, $*/

require(['./lib/knockout',
		 './config/global',		 
		 './models/Account',
		 './viewModels/account',
		 './lib/require-jquery',
		 './lib/jquery.cookie',
		 './extends/handlers',
		 './lib/knockout-amd-helpers'], function(ko, g, Account, AccountViewModel) {
	
	'use strict';

	// TODO: dar focus no userName quando for aberto o modal login
	// TODO: trabalhar no lembrar-me quando for guardar pra valer o nome de usuário
	//var todos = ko.utils.parseJson(window.localStorage.getItem(g.localStorageItem));
	var account = new Account($.cookie('auth'), '');
	ko.applyBindings(new AccountViewModel(account));
	console.log(ko);
});