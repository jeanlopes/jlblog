/*global require, console, $*/

define(['./lib/knockout',
		 './config/global',		 
		 './models/Account',
		 './viewModels/account',
		 './lib/jquery.min',
		 './lib/jquery.cookie',
		 './extends/handlers',
		 './lib/knockout-amd-helpers',
		 './text',
		 './lib/bootstrap'], function(ko, g, Account, AccountViewModel) {
	
	//'use strict';

	// TODO: dar focus no userName quando for aberto o modal login
	// TODO: trabalhar no lembrar-me quando for guardar pra valer o nome de usuário

    var Common = function () {

        var self = this;

        self.account = new Account($.cookie('auth') || '', '');
        self.accountViewModel = new AccountViewModel(self.account);
        //

        self.applyBindings = function (viewModel){

            if (viewModel)
            {
                for (var prop in self.accountViewModel)
                    viewModel[prop] = self.accountViewModel[prop];

                //Object.defineProperty(viewModel, 'accountViewModel', { 'value': self.accountViewModel });
                ko.applyBindings(viewModel);
            }
            else
                ko.applyBindings(self.accountViewModel);
        };
    };

    return Common;

});