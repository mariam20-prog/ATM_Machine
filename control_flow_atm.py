# bin/bash
import sys 
from typing import Tuple

class ATM:
    def __init__(self, initial_balance=5000, pin=2421):
        self.balance = initial_balance
        self.pin = pin
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.max_attemps = 3

        def Verify_pin(self, user_pin):
            """Verify user PIN with limited attempts."""
            attempts = 0
            while attempts < self.attempts: 
                try:
                    user_pin = int(input("Enter your PIN: "))
                    if user_pin == self.pin:
                        return True
                    attempts += 1
                    print(f'Incorrect PIN {self.attempts - attempts} attempts remaining')
                except ValueError:
                    print("Invaild input. PIN must be a number.")
                    attempts += 1

                    print("Too many incorrect attempts. Access blocked.")
                    return False
                
                def check_balance(self) -> None:
                    """Display current balance."""
                    print(f"\nCurrent Balance: $ {self.balance:.2f}")

                    def deposit(self) -> None:
                        """Handle deposit operation with input validation."""
                        while True:
                            try:
                                amount = float(input("\nEnter amount to deposit:$"))
                                if amount <= 0:
                                    print("Amount must be positive.")
                                    continue
                                self.balance += amount
                                self.total_deposits += amount
                                print(f"Deposit successful. New balance: $ {self.balance:.2f}")
                                break
                            except ValueError:
                                print("Invalid input. Please enter a number.")

                                def withdraw(self) -> None:
                                    """Handle withdrawal operation with balance verification."""
                                    while True:
                                        
                                            amount = float(input("\nEnter amount to withdraw: $"))
                                            if amount <= 0:
                                                print("Amount must be positive.")
                                                continue
                                            if amount > self.balance: print("Insufficient funds.")
                                            continue 
                                    self.balance -= amount
                                    self.total_withdrawals += amount
                                    print(f"withdrawal successful. New balance: $ {self.balance:.2f}")
                                    
                            except ValueError:
                                print("invalid input. Please enter a number.")

                                def change_pin(self) -> None:
                                    """Change PIN with verification steps."""
                                    
                                    current_pin =int(input("\nEnter current PIN: "))
                                    if current_pin != self.pin:
                                        print("Incorrect PIN.")
                                        return
                                    
                                    while True:
                                        new_pin = input("ENter new 4-digit PIN: ")
                                        if not (new_pin.isdigit() and len(new_pin) == 4):
                                            print("PIN must be a 4-digit number.")
                                            continue

                                        confirm_pin = input("Confirm new PIN: " )
                                        if new_pin != confirm_pin: 
                                            print("PINs do not match.")
                                            continue

                                        self.pin = int(new_pin)
                                        print("PIN successfully changed.")
                                        break

                             
                            except ValueError:
                                print("Invalid input. PIN must be a number.")

                                def display_menu(self) -> None:
                                    """Display main menu options."""
                                    print("\n=== ATM Menu ===")
                                    print("1. Check Balance")
                                    print("2. Deposit Funds")
                                    print("3. Withdraw Funds")
                                    print("4. Change PIN")
                                    print("5. Exit")

                                    def run(self) -> None:
                                        """Main ATM operation loop."""
                                        if not self.authenticate():
                                            return
                                        
                                    while True:
                                            self.display_menu()
                                            
                                            choice = input("\nEnter your choice (1-5): ")

                                            if choice =='1':
                                                self.check_balance()
                                            elif choice =='2':
                                                self.deposit()
                                            elif choice =='3':
                                                self.withdraw()
                                            elif choice =='4':
                                                self.change_pin()
                                            elif choice =='5':
                                                self.show_summary()
                                                break
                                            else:
                                                print("Invalid choice. Please select 1-5.")
                                                
                               
                                def show_summary(self) -> None:
                                    """Display transaction summary when existing"""
                                    print("\n=== Transcations Summary ===")
                                    print(f"Total Deposits: $ {self.total_deposits:.2f}")
                                    print(f"Total Withdrawals: $ {self.total_withdrawls:.2f}")
                                    print("Thank you for using our ATM. Goodbye!")

                                def main():
                                        """Entry point of the program."""
                                        atm = ATM()
                                        print("Welcome to the ATM Machine")
                                        atm.run()

                                        if __name__=="__main__": 
                                            main() 

                                        

                                                             

                                    







                                         

                                    












# ATM_Machine
