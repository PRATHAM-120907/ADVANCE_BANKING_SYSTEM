# Banking Management System Practice

accounts = {}

def print_header():
    print("=" * 50)
    print("         WELCOME TO THE XYZ BANK")
    print("=" * 50)

def print_menu():
    print("\n" + "-" * 50)
    print("1) Create account")
    print("2) Deposit money")
    print("3) Withdraw amount")
    print("4) Display the account")
    print("5) Exit")
    print("-" * 50)

def create_account(account_number, holder_name, balance, password):
    if len(str(account_number)) < 8:
        print("ACCOUNT NUMBER MUST BE AT LEAST 8 DIGITS.")
        return
    if len(str(password)) != 4 or not str(password).isdigit():
        print("PASSWORD MUST BE EXACTLY 4 DIGITS.")
        return
    if balance < 2000:
        print("MINIMUM BALANCE TO OPEN AN ACCOUNT IS 2000.")
        return
    accounts[account_number] = {
        "holders_name": holder_name,
        "balance": balance,
        "password": str(password)
    }
    print(f"\n{'*' * 50}")
    print(f"ACCOUNT {account_number} HAS BEEN CREATED FOR {holder_name.upper()} WITH THE BALANCE OF {balance}")
    print(f"{'*' * 50}")

def verify_password(account_number):
    if account_number not in accounts:
        print("ACCOUNT NOT FOUND")
        return False
    password = input("ENTER YOUR 4-DIGIT ACCOUNT PASSWORD:\n")
    if password == accounts[account_number]['password']:
        return True
    else:
        print("INCORRECT PASSWORD.")
        return False

def deposit(account_number, amount):
    if account_number in accounts:
        if verify_password(account_number):
            accounts[account_number]['balance'] += amount
            print(f"\nDEPOSITED {amount} TO THE ACCOUNT NUMBER {account_number}")
    else:
        print("ACCOUNT NOT FOUND")

def withdraw(account_number, amount):
    if account_number in accounts:
        if verify_password(account_number):
            if accounts[account_number]['balance'] >= amount:
                accounts[account_number]['balance'] -= amount
                print(f"\nTHE AMOUNT {amount} IS DEDUCTED FROM ACCOUNT NUMBER {account_number}")
            else:
                print("INSUFFICIENT BALANCE")
    else:
        print("ACCOUNT NOT FOUND")

def display_account(account_number):
    if account_number in accounts:
        if verify_password(account_number):
            print("\n" + "=" * 50)
            print(f"ACCOUNT NUMBER : {account_number}")
            print(f"HOLDER'S NAME  : {accounts[account_number]['holders_name'].upper()}")
            print(f"BALANCE        : {accounts[account_number]['balance']}")
            print("=" * 50)
    else:
        print("ACCOUNT NOT FOUND")

def main():
    print_header()
    while True:
        print_menu()
        choice = int(input("ENTER THE VALID NUMBER FOR YOUR USAGE:\n"))

        if choice == 1:
            account_number = int(input("PLEASE ENTER THE ACCOUNT NUMBER (MINIMUM 8 DIGITS):\n"))
            holder_name = input("ENTER THE OWNER/HOLDER'S NAME:\n").strip()
            balance = float(input("ENTER THE AMOUNT TO OPEN THE ACCOUNT (MINIMUM 2000):\n"))
            password = input("SET A 4-DIGIT NUMERIC PASSWORD FOR YOUR ACCOUNT:\n")
            create_account(account_number, holder_name, balance, password)
        elif choice == 2:
            account_number = int(input("PLEASE ENTER THE ACCOUNT NUMBER:\n"))
            amount = float(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:\n"))
            deposit(account_number, amount)
        elif choice == 3:
            account_number = int(input("PLEASE ENTER YOUR ACCOUNT NUMBER:\n"))
            amount = float(input("ENTER THE AMOUNT TO WITHDRAW:\n"))
            withdraw(account_number, amount)
        elif choice == 4:
            account_number = int(input("PLEASE ENTER YOUR ACCOUNT NUMBER:\n"))
            display_account(account_number)
        elif choice == 5:
            print("\n" + "=" * 50)
            print("Thank you for using XYZ Banking System.")
            print("=" * 50)
            break
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")

if __name__ == "__main__":
    main()

