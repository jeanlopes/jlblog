
$(document).ready(function() {    
    ko.applyBindings({accountViewModel: new accountViewModel(), postModel : new postModel(),  interestsListModel : new interestsListModel()  });
    
    $('#modalLogin').on('shown', function() {
        $("#user").focus();
    })    
});

if (window.interestsListModel === undefined) {
	console.log('InterestsListModel undefined');
    window.InterestsListModel = function() { }
}

if (window.postModel === undefined) {
    window.postModel = function() { }
}


function accountViewModel () {
    
    var self = this;
    

    self.user = ko.observable($.cookie('auth') === undefined ||  $.cookie('auth') == null ? '' : $.cookie('auth'));
    self.password = ko.observable('');
    self.logged = ($.cookie('auth') === undefined ||  $.cookie('auth') == null) ? false : true;
    
    
    self.login = function () {
    //console.log(self.user());
         $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:5000/login',
            data: {
            	'csrf_token': $('#csrf_token').val(), 
                'user': self.user(),
                'password': self.password()
                },
            success: function(data){
                if (data.success == 'true') {
                    window.location.replace('admin');
                    $.cookie('auth', self.user());
                }
                else
                for (var error in data.errors)
                    alert(error +': '+ data.errors[error]);
            },
            dataType: 'json'
        }); 
    };

    self.selectTemplate = function() {    
        return self.logged == false ? "loginTemplate" : "dropdownTemplate";
    };

    self.forgot = function () {
        alert('te fode guerreiro!');
    };

    self.logout = function() {
        $.removeCookie('auth', null);
        self.user(null);
        self.logged = false;
        window.location.replace('home');
    }
}

