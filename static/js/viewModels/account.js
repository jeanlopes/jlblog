/*global define, window*/
define(['../lib/knockout', '../config/global', '../models/Account', '../lib/require-jquery'], function(ko, g, Account, $) {
	
	var AccountViewModel = function(account) {


		var self = this;
		
		/**
		 * @property se existem mensagens
		 */
		self.hasMessage = ko.observable(false);
		
		/**
		 * @property lista de mensagens de erro
		 */
		 self.errorsMessage = ko.observableArray([]);
		
		/**
		 * @function verifica se o usuário está logado
		 */
		self.isLogged = function() {			
			
			if ($.cookie('auth'))
				return true;
			return false;
		};
		
		
		/**
		 * @function faz login no blog
		 */
		self.login = function() {
		
			// TODO: substituir com text.js
			$.ajax({
				type : "POST",
				url : '/login',
				data : {
					'csrf_token' : $('#csrf_token').val(),
					'user' : self.user(),
					'password' : self.password()
				},
				success : function(data) {
					if (data.success == 'true') {
						window.location.replace('admin');
						$.cookie('auth', self.user());
					} else {
						//TODO: criar binds nos html
						// http://knockoutjs.com/documentation/visible-binding.html
						self.hasMessage(true);
						for (var error in data.errors) {
							self.errorsMessage.push(error + ': ' + data.errors[error]);
						}
						window.alert(error + ': ' + data.errors[error]);
					}
				},
				dataType : 'json'
			});
		};


		/**
		 * @function seleciona o template de acordo com o usuário logado ou deslogado
		 */
		self.selectTemplate = function() {
			return self.isLogged() == false ? "loginTemplate" : "dropdownTemplate";
		};
		
		
		/**
		 * @function se o usuário perdeu a senha manda ele se foder
		 */
		self.forgot = function() {
			window.alert('te fode guerreiro!');
		};
		
		
		/**
		 * @function desloga do blog
		 */
		self.logout = function() {
			$.removeCookie('auth', null);
			self.user(null);
			self.logged = false;
			window.location.replace('home');
		};
	};
	
	return AccountViewModel;
});
