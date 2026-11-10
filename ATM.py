# Simple ATM Menu System

# Predefined PIN and starting balance
correct_pin = "1234"
balance = 1000.00

# PIN Authentication
pin = input("Enter your ATM PIN: ")

if pin == correct_pin:
    print("\nAccess Granted!")
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = input("\nSelect an option (1-3): ")

    # Option 1: Check Balance
    if choice == "1":
        print(f"\nYour current balance is: R{balance:.2f}")

    # Option 2: Deposit Money
    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit: R"))

        if deposit_amount > 0:
            balance += deposit_amount
            print("Deposit successful!")
            print(f"Updated balance: R{balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    # Option 3: Withdraw Money
    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw: R"))

        if withdraw_amount <= 0:
            print("Invalid withdrawal amount. Amount must be greater than zero.")
        elif withdraw_amount > balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            balance -= withdraw_amount
            print("Withdrawal successful!")
            print(f"Updated balance: R{balance:.2f}")

    # Invalid Option
    else:
        print("Invalid menu option selected.")

# Incorrect PIN
else:
    print("Incorrect PIN. Access denied.")