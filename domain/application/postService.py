from domain.repositories.postRepository import PostRepository

__author__ = 'jean'


class PostService:

    def __init__(self, post):
        self.repository = PostRepository(post)

    def create(self):
        self.repository.create()

    def save(self):
        #self.repository.sa
        pass

    def delete(self):
        pass

    def set_published(self, value):
        if type(value) != bool:
            raise NameError('O valor passado deve ser booleano - Valor passado: ' + str(type(value)))
        self.repository.set_published(value)