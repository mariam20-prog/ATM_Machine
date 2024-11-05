#!/usr/bin/env python3
# ATM_Machine

# Initial Setup
balance = 10000
total_deposits = 0
total_withdrawals = 0
attempts = 0
max_attempts = 3

# Stored data for username and PIN
user_data = {
    'Mariam': 2421,  # Username: PIN
    'Beatrice': 2468
}

def authenticate_user():
    global attempts
    while attempts < max_attempts:
        username = input("Enter your username: ")
        if username in user_data:
            entered_pin = input("Enter your PIN: ")
            if entered_pin.isdigit() and int(entered_pin) == user_data[username]:
                print(f"Welcome, {username}!")
                return username  # Return the username for further use
            else:
                attempts += 1
                if attempts == max_attempts:
                    print("Too many incorrect attempts. Access blocked.")
                    return None
                else:
                    print(f"Incorrect PIN. {max_attempts - attempts} attempts remaining.")
        else:
            print("Username not found. Please try again.")
    return None

def check_balance(username):
    print(f"Current balance for {username}: ${balance:.2f}")

def deposit_funds(username):
    global balance, total_deposits
    amount = input("Enter amount to deposit: ")
    if amount.isdigit() and int(amount) > 0:
        balance += int(amount)
        total_deposits += int(amount)
        print(f"Deposited: ${amount}. New balance for {username}: ${balance:.2f}")
    else:
        print("Invalid amount. Please enter a positive number.")

def withdraw_funds(username):
    global balance, total_withdrawals
    amount = input("Enter amount to withdraw: ")
    if amount.isdigit() and int(amount) > 0:
        if int(amount) <= balance:
            balance -= int(amount)
            total_withdrawals += int(amount)
            print(f"Withdrawn: ${amount}. New balance for {username}: ${balance:.2f}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid amount. Please enter a positive number.")

def change_pin(username):
    global user_data
    current_pin = input("Enter your current PIN: ")
    if current_pin.isdigit() and int(current_pin) == user_data[username]:
        new_pin = input("Enter your new 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            confirm_pin = input("Confirm your new PIN: ")
            if confirm_pin == new_pin:
                user_data[username] = int(new_pin)
                print("PIN changed successfully.")
            else:
                print("PINs do not match.")
        else:
            print("New PIN must be a 4-digit integer.")
    else:
        print("Current PIN is incorrect.")

def main():
    username = authenticate_user()
    if username:
        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Change PIN")
            print("5. Exit")
            choice = input("Select an option (1-5): ")

            if choice == '1':
                check_balance(username)
            elif choice == '2':
                deposit_funds(username)
            elif choice == '3':
                withdraw_funds(username)
            elif choice == '4':
                change_pin(username)
            elif choice == '5':
                print(f"Thank you for using the ATM, {username}. You deposited ${total_deposits} and withdrew ${total_withdrawals}.")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Access Denied.")

if __name__ == "__main__":
    main()