from wtforms.widgets.core import html_params
import re, htmlentitydefs

def list_widget(**kwargs):
    
    div_class = kwargs.pop('div_class')
    field_model = kwargs.pop('model')
    field_id_select = kwargs.pop('id_select')
    html = [u'<div  %s>' % html_params(**{'data-bind': 'with: $root.' + field_model, 'class': div_class})]
    html.append(u'<input %s/>' % html_params(**{'type':'text','data-bind': "value:itemToAdd, valueUpdate: 'afterkeydown'"}))
    html.append(u'<button %s>' % html_params(**{'data-bind':'enable: itemToAdd().length > 0, click: addItem'}))
    html.append(u'Adicionar')
    html.append(u'</button>')
    html.append(u'<p>Seus interesses</p>')
    html.append(u'<select %s>' % html_params(**{'id': field_id_select, 'name': field_id_select,'multiple': 'multiple', 'height': 5, 'data-bind': 'options:allItems, selectedOptions:selectedItems'}))
    html.append(u'</select>')
    html.append(u'<div>')
    html.append(u'<button %s>' % html_params(**{'data-bind':'click: removeSelected, enable: selectedItems().length > 0'}))
    html.append(u'Remover')
    html.append(u'</button>')        
    html.append(u'</div>')
    html.append(u'</div>')
   
    return unescape(u''.join(html))


# http://effbot.org/zone/re-sub.htm#unescape-html
##
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

