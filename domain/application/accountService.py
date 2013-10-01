from domain.entities.Account import Account
from domain.repositories.accountRepository import AccountRepository


class AccountService:

    def __init__(self, account):
        self.repository = AccountRepository(account)

    def get_by_username(self, username):

        if type(username) != unicode:
            raise NameError('O valor passado deve ser um unicode - Valor passado: ' + str(type(username)))

        result = self.repository.get_by_username()

        if len(result) == 0:
            return result

        doc = Account.wrap(result)
        doc.id = result.get('_id')

        return doc