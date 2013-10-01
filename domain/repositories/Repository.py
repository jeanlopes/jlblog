# coding=utf-8
from couchdbkit import Document
from domain.data.context import Context

__author__ = 'jean'


class Repository(Document):

    """
    Classe que implementa métodos básicos a todos os repositórios
    """

    def __init__(self, entity):
        self.context = Context()

        self.entity = entity
        self.entity.set_db(self.context.db)

    def create(self):
        self.entity.save()

    def update(self):

        doc = self.entity.get(self.entity.id, db=self.context.db)
        for g in self.entity.items():
            doc[g[0]] = g[1]
        doc.save()

    def remove(self):
        self.context.db.delete_doc(self.entity)

    #TODO: verificar se self.entity retorna o nome da entidade
    def list(self):
        return self.context.db.view('main/entities', self.entity)

    def get_by_id(self, _id, entity):

        assert entity.__class__ == Document.__class__

        if type(_id) != unicode:
            raise NameError('O valor passado deve ser um unicode - Valor passado: ' + str(type(_id)))

        return entity.get(_id, db = self.context.db)