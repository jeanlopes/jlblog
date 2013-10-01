from domain.repositories.Repository import Repository

__author__ = 'jean'


class AccountRepository(Repository):

    def __init__(self, account):
        self.account = account
        super(AccountRepository, self).__init__(account)

    def get_by_username(self):

        res = None
        try:
            res = self.context.db.list('main/entities', 'accounts', key=self.account.username)

        except():
            pass
            #TODO: terminar isso
            #return new CouchdbkitException...

        return res