function addSyntaxHighlighter() {

    $('ul.k-editor-toolbar').parent().append('<li style="list-style-type: none;" class="k-editor-select-box" data-bind="template: {name:\'syntaxHighlighterDropdown\'}"></li>');
    
    //ko.applyBindings(new syntaxModel(), $('html')[0]);
    //$('html').data('syntaxModel',syntaxModel);
}

function postModel() {

    var self = this;

    self.insertSyntax = function (value1, value2) {
        var t = $('table.k-editor iframe').contents().find('body');        
        t.append(' &#60;pre class="brush: '+ $('#highlighter').val() +';"&#62;&#60;/pre&#62;');
        $('#highlighter').val('');
    }
}

$(document).ready(function() {
	$('#editor').kendoEditor();
        addSyntaxHighlighter();
        
})