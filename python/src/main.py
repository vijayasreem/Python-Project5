# i'm creating a banking management system
import datetime
import random
import uuid
import sqlite3
i

def name():
    input_name = input("Enter your name: ")
    if input_name.isalpha():
        return input_name
    else:
        print("Invalid Name, Only Alphabets Allowed")
        name()

def age():
    input_age = int(input("Enter your age: "))
    if input_age < 18:
        print("You are not eligible to create an account")
        exit()
    elif input_age > 18:
        return input_age
    

def adress():
    # TODO : check if adress is valid
    input_adress = input("Enter your adress: ")
    return input_adress

def phone_number():
    prefix = input("Enter the prefix for your phone number : ")
    if len(str(prefix)) == 3:
        pass
    else:
        print("Invalid Prefix, Only 3 Digits Allowed")
        phone_number()
    input_phone_number = int(input("Enter the remaining digits of your phone number: "))
    if len(str(input_phone_number)) == 7:
        return prefix + str(input_phone_number)
    else:
        print("Invalid Phone Number, Only 7 Digits Allowed")
        phone_number()


def id_generator():
    unique_id = str(uuid.uuid4())
    return unique_id

def balance():
    if balance == None:
        return 0
    else:
        return f"Your balance is {balance}$"

def welcome(user_name, user_id, user_balance):
    return f"""
    Welcome {user_name} to Kernel Bank 🏦  :
    Your ID is {user_id}
    Your Balance is {user_balance}
    Your Account was created on {datetime.datetime.now()}
    if you want to edit your account details
    if you have any questions, please contact us at Kernel-rb on github
    """

def create_account():
    print("Creating Account")
    user_name = name()
    user_age  = age()
    user_adress  = adress()
    user_phone_number = phone_number()
    user_id = id_generator()
    user_balance = balance()
    user_welcome_message = welcome(user_name, user_id, user_balance)


def main():
    print(
        """
    Welcome to Kernel Bank 🏦  : 
    1. Create Account
    2- Edit Account Details
    3. Deposit Money
    4. Withdraw Money
    5. Check Balance
    6. Display Account Details
    7. Transfer Money
    8. Delete Account
    9. Exit
        """
    )
    choice = input("Enter your choice: ")
    if type(choice) == int:
        if choice == 1:
            create_account()
        elif choice == 2:
            edit_account_details()
        elif choice == 3:
            deposit_money()
        elif choice == 4:
            withdraw_money()
        elif choice == 5:
            check_balance()
        elif choice == 6:
            display_account_details()
        elif choice == 7:
            transfer_money()
        elif choice == 8:
            delete_account()
        elif choice == 9:
            exit()
    else:
        print("Invalid Choice , Only Numbers Allowed")