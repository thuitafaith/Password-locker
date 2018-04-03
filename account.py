class Account:
    '''
    class that generates new instances of accounts
    '''
    account_list = [] #Empty account list
    def save_account(self):

         Account.account_list.append(self)
    def delete_account(self):

        Account.account_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        for account in cls.account_list:
            if account.email == email:
                return account
    def __init__(self,first_name,last_name,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
