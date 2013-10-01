from domain.repositories.Repository import Repository

__author__ = 'jean'

from domain.data.context import Context


class PostRepository(Repository):

    def __init__(self, post):
        self.post = post
        super(PostRepository, self).__init__(post)
        self.context = Context

    def is_published(self):
        return self.post.is_published

    def set_published(self, value):
        self.post.is_published = value