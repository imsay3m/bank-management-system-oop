class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def check_accounts(self):
        self.bank.admin_check_accounts()

    def total_balance(self):
        self.bank.admin_total_balance()

    def total_loan_amount(self):
        print(f"Total loan amount: {self.bank.total_loan_amount}")

    def loan_feature_on_off(self):
        self.bank.admin_loan_feature()
