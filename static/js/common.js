/*global require, console, $*/

require(['./lib/knockout',
		 './config/global',		 
		 './models/Account',
		 './viewModels/account',
		 './lib/jquery.min',
		 './lib/jquery.cookie',
		 './extends/handlers',
		 './lib/knockout-amd-helpers',
		 './text',
		 './lib/bootstrap'], function(ko, g, Account, AccountViewModel) {
	
	'use strict';

	// TODO: dar focus no userName quando for aberto o modal login
	// TODO: trabalhar no lembrar-me quando for guardar pra valer o nome de usuário

	var account = new Account($.cookie('auth') || '', '');
	var accountViewModel = new AccountViewModel(account);
	ko.applyBindings(accountViewModel);
	//console.log(ko.dataFor(document.body));
});