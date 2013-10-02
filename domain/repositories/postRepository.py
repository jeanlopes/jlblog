from domain.entities.Post import Post
from domain.repositories.Repository import Repository

__author__ = 'jean'

from domain.data.context import Context


class PostRepository(Repository):

    def __init__(self, post=None):
        if post:
            self.post = post

        super(PostRepository, self).__init__(post)
        self.context = Context

    def is_published(self):
        return self.post.is_published

    def set_published(self, value, _id=None):

        if _id:
            self.post = self.get_by_id(_id, Post)
        self.post.is_published = value
        self.post.save()