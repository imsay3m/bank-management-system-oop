class User:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        self.bank.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        self.bank.withdraw(account_number, amount)

    def check_balance(self, account_number):
        self.bank.check_balance(account_number)

    def transfer_balance(self, from_account, to_account, amount):
        self.bank.transfer_balance(from_account, to_account, amount)

    def loan(self, account_number, amount):
        self.bank.loan(account_number, amount)

    def transaction_history(self, account_number):
        self.bank.transaction_history(account_number)
