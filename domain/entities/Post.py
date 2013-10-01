from couchdbkit.schema.properties import StringProperty, DateTimeProperty, DictProperty, BooleanProperty, ListProperty
from domain.entities.Entity import Entity
from datetime import datetime
__author__ = 'jean'


class Post(Entity):

    def __init__(self, author='', date=datetime.now(), content={}, is_published=False, keywords=[]):

        self.author = StringProperty(author)
        self.date = DateTimeProperty(date)
        self.content = DictProperty(content)
        self.is_published = BooleanProperty(is_published)
        self.keywords = ListProperty(keywords)