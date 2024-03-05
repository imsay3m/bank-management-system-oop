from Admin import Admin
from Bank import Bank
from User import User


def admin_operations(admin):
    print("\nAdmin Operations:")
    print("1. Check Accounts")
    print("2. Total Balance")
    print("3. Loan Feature On/Off")
    print("4. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        admin.check_accounts()
    elif choice == "2":
        admin.total_balance()
    elif choice == "3":
        admin.loan_feature_on_off()
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")
    admin_operations(admin)


def main():
    bank = Bank()
    admin = Admin(bank)
    user = User(bank)

    while True:
        print("\nWelcome to the Bank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Balance")
        print("5. Check Balance")
        print("6. Take Loan")
        print("7. View Transaction History")
        print("8. Admin Operations")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            while True:
                account_type = input(
                    "Enter account type number (1.Savings/2.Current): "
                )
                if account_type in ["1", "2"]:
                    account_type = account_type
                    break
                else:
                    print("Please enter a valid number (1 for Savings, 2 for Current)")
            user.create_account(name, email, address, account_type)

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            user.deposit(account_number, amount)

        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(account_number, amount)

        elif choice == "4":
            from_account = int(input("Enter your account number: "))
            to_account = int(input("Enter recipient's account number: "))
            amount = float(input("Enter amount to transfer: "))
            user.transfer_balance(from_account, to_account, amount)

        elif choice == "5":
            account_number = int(input("Enter account number: "))
            user.check_balance(account_number)

        elif choice == "6":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter loan amount: "))
            user.loan(account_number, amount)

        elif choice == "7":
            account_number = int(input("Enter account number: "))
            user.transaction_history(account_number)

        elif choice == "8":
            admin_operations(admin)

        elif choice == "9":
            print("\n---------Goodbye----------\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
