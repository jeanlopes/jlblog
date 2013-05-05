from wtforms.widgets.core import html_params


def list_widget(**kwargs):
    
    div_class = kwargs.pop('div_class')
    field_model = kwargs.pop('model')
    field_id_select = kwargs.pop('id_select')
    html = [u'<div %s>' % html_params(**{'data-bind': field_model, 'class': div_class})]    
    html.append(u'Adicionar interesse')
    html.append(u'<input %s/>' % html_params(**{'type':'text','data-bind': 'value:itemToAdd, valueUpdate: "afterkeydown"'}))
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
   
    return u''.join(html)