import random


class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(10000, 99999)

        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)

        if account_type == "1":
            ACCOUNT_TYPE = "Savings"
        else:
            ACCOUNT_TYPE = "Current"

        new_account = {
            "name": name,
            "email": email,
            "address": address,
            "account_type": ACCOUNT_TYPE,
            "account_number": account_number,
            "balance": 0,
            "loan_count": 0,
            "transactions_history": [],
        }

        self.accounts[account_number] = new_account
        print(
            "Please Copy the number\nAccount created successfully with account number: ",
            account_number,
        )

    def delete_account(self, account_number):
        account_details = self.accounts.pop(account_number, None)
        if account_details:
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Invalid amount.")
            return
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transactions_history"].append(
                f"Deposited {amount} to {account_number}"
            )
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Invalid amount.")
            return

        if account_number in self.accounts:
            if self.is_bankrupt():
                print("The bank is bankrupt.")
            else:
                if self.accounts[account_number]["balance"] >= amount:
                    self.accounts[account_number]["balance"] -= amount
                    self.accounts[account_number]["transactions_history"].append(
                        f"Withdrew {amount} from {account_number}"
                    )
                    print("Withdraw successful.")
                else:
                    print("There is not enoungh money in your account.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            print(f"Current balance is: {balance}")
        else:
            print("Account not found.")

    def transfer_balance(self, from_account, to_account, amount):
        if amount <= 0:
            print("Invalid amount.")
            return
        if from_account in self.accounts and to_account in self.accounts:
            if self.is_bankrupt():
                print("The bank is bankrupt.")
            else:
                if self.accounts[from_account]["balance"] >= amount:
                    self.accounts[from_account]["balance"] -= amount
                    self.accounts[to_account]["balance"] += amount
                    self.accounts[from_account]["transactions_history"].append(
                        f"Transferred {amount} from {from_account} to {to_account}"
                    )
                    self.accounts[to_account]["transactions_history"].append(
                        f"Transferred {amount} from {to_account} to {from_account}"
                    )
                    print("Transfer successful.")
                else:
                    print("Insufficient balance to transfer.")
        else:
            print("One or both accounts not found.")

    def loan(self, account_number, amount):
        if amount <= 0:
            print("Invalid loan amount.")
            return

        if account_number in self.accounts:
            if self.loan_feature:
                if self.accounts[account_number]["loan_count"] < 2:
                    self.accounts[account_number]["loan_count"] += 1
                    self.accounts[account_number]["balance"] += amount
                    self.total_balance += amount
                    self.accounts[account_number]["transactions_history"].append(
                        f"Loan taken: {amount}"
                    )
                    print("Loan successful.")
                else:
                    print("You have already taken the maximum number of loans.")
            else:
                print("Loan feature is currently disabled. Contact Admin.")
        else:
            print("Account not found.")

    def transaction_history(self, account_number):
        if account_number in self.accounts:
            print("Transaction History")
            for transaction in self.accounts[account_number]["transactions_history"]:
                print(transaction)
        else:
            print("Account not found.")

    def admin_check_accounts(self):
        print("All User Accounts:")
        for account_number, details in self.accounts.items():
            print(f"Account Number: {account_number}")
            print(f"Name: {details['name']}")
            print(f"Email: {details['email']}")
            print(f"Account Type: {details['account_type']}")
            print(f"Balance: {details['balance']}")
            print("\n,,,,,,,,,,,,,,,,,,,,,,,,,,\n")

    def admin_total_balance(self):
        print(f"Total balance of the bank: {self.total_balance}")

    def admin_loan_feature(self):
        self.loan_feature = not self.loan_feature
        if self.loan_feature:
            status = "enabled"
        else:
            status = "disabled"
        print(f"Loan is now {status}")

    def is_bankrupt(self):
        if self.total_balance < 0:
            return True
        else:
            return False

    def check_bankruptcy(self):
        if self.is_bankrupt():
            print("The bank is currently bankrupt.")
        else:
            print("The bank is financially stable.")
