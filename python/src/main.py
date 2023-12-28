import os
import datetime
import random
import uuid
import sqlite3
import logging
from email_validator import validate_email, EmailNotValidError
from colorama import Fore, Style, init
import qrcode
import webbrowser

# colorma Setup
init(autoreset=True)
# Logs Setup
log_dir = "C:\\Users\\petmk\\Desktop\\BankingManagement\\python\\log"
log_file = os.path.join(log_dir, "main.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s\n' + ('=' * 50) + '\n')
logging.info("Logging is working")
logging.info("Program Started")

def name():
    while True:
        input_name = input("Enter your name: ")
        if input_name.isalpha():
            logging.info(f"User name is {input_name}")
            return input_name
        else:
            print("Invalid Name, Only Alphabets Allowed")
            logging.error("Invalid Name, Only Alphabets Allowed")

def age():
    input_age = int(input("Enter your age: "))
    if input_age < 18:
        print("You are not eligible to create an account")
        logging.error("You are not eligible to create an account")
        exit()
    elif input_age >= 18:
        logging.info(f"User is {input_age} years old")
        return input_age

def gmail():
    input_gmail = input("Enter your gmail: ")
    logging.info(f"User gmail is {input_gmail}")
    return input_gmail

def check(input_gmail):
    try:
        if not input_gmail:
            exit()
        v = validate_email(input_gmail, check_deliverability=False)
        validated_email = v["email"]
        if not v.is_valid():
            logging.error(f"The provided email '{input_gmail}' is not valid.")
            raise EmailNotValidError(input_gmail)
        return validated_email
    except EmailNotValidError as e:
        print(f"{Fore.RED}Invalid email. Please try again.{Style.RESET_ALL}")
        logging.error("Invalid email entered by the user.")
        raise

def address():
    input_address = input("Enter your address: ")
    logging.info(f"User address is {input_address}")
    return input_address

def phone_number():
    while True:
        prefix = input("Enter the prefix for your phone number: ")
        if len(str(prefix)) == 3:
            logging.info(f"User phone number prefix is {prefix}")
        else:
            print("Invalid Prefix, Only 3 Digits Allowed")
            logging.error("Invalid Prefix, Only 3 Digits Allowed")
            continue

        input_phone_number = int(input("Enter the remaining digits of your phone number: "))

        if len(str(input_phone_number)) == 7:
            logging.info(f"User phone number is {prefix + str(input_phone_number)}")
            return prefix + str(input_phone_number)
        else:
            print("Invalid Phone Number, Only 7 Digits Allowed")
            logging.error("Invalid Phone Number, Only 7 Digits Allowed")

def id_generator():
    unique_id = str(uuid.uuid4())
    logging.info(f"User ID is {unique_id}")
    return unique_id

def balance():
    logging.info(f"User Balance is {0}")
    return 0

def welcome(user_name, user_id, user_balance):
    welcome_message = f"""
    Welcome {user_name} to Kernel Bank 🏦  :
    Your ID is {user_id}
    Your Balance is {user_balance}
    Your Account was created on {datetime.datetime.now()}
    If you want to edit your account details
    If you have any questions, please contact us at Kernel-rb on GitHub
    """
    logging.info("All User Details")
    logging.info(f"User Welcome Message: {welcome_message}")
    return welcome_message

def qr_code(user_id, user_name, user_gmail):
    data = f"""
        Welcome {user_name} to Kernel Bank 🏦  :
        Your ID is {user_id}
        Your gmail is {user_gmail}
        If you want to edit your account details , click on the link below
        If you have any questions, please contact us at Kernel-rb on GitHub
        """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="green")
    img.save("qrcode.png")
    print("QR Code Generated Successfully")
    return os.path.abspath("qrcode.png")

def create_account():
    print("Creating Account...")
    user_name = name()
    user_age = age()
    while True:
        try:
            user_gmail = gmail()
            user_gmail = check(user_gmail)
            break  
        except EmailNotValidError as e:
            print(f"{Fore.GREEN}Invalid email: {e}{Style.RESET_ALL}")
            logging.error(f"Invalid email: {e}")
    user_phone_number = phone_number()
    user_address = address()
    user_id = id_generator()
    user_balance = balance()
    user_welcome_message = welcome(user_name, user_id, user_balance)
    print(user_welcome_message)
    logging.info("User Account Created Successfully")
    qr_code_path = qr_code(user_id, user_name, user_gmail)
    web_page_content = f"<html><body><img src='file://{qr_code_path}'></body></html>"
    web_page_path = "QrCode.html"
    with open(web_page_path, "w") as web_page:
        web_page.write(web_page_content)
    webbrowser.open("file://" + os.path.abspath(web_page_path))

def edit_account_details():
    pass

def deposit_money():
    pass

def withdraw_money():
    account_number = input("Enter your account number: ")
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    current_balance = 1000.00  # Placeholder for current balance, replace with actual balance retrieval from database
    withdrawal_limit = 500.00  # Placeholder for withdrawal limit, replace with actual limit retrieval from database

    if withdrawal_amount > current_balance:
        print("Error: Insufficient balance")
        logging.error("Insufficient balance for withdrawal")
    elif withdrawal_amount > withdrawal_limit:
        print("Error: Withdrawal amount exceeds limit")
        logging.error("Withdrawal amount exceeds limit")
    else:
        new_balance = current_balance - withdrawal_amount
        print(f"Withdrawal successful. New balance: {new_balance}")
        logging.info(f"Withdrawal successful. New balance: {new_balance}")

def check_balance():
    pass

def display_account_details():
    pass

def transfer_money():
    pass

def delete_account():
    pass

def main():
    logging.info("Program Started")
    print(
        """
    Welcome to Kernel Bank 🏦  : 
    1. Create Account
    2. Edit Account Details
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
    logging.info(f"User Choice is {choice}")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            create_account()
            logging.info("User Account Created Successfully")
        elif choice == 2:
            edit_account_details()
            logging.info("User Account Details Edited Successfully")
        elif choice == 3:
            deposit_money()
            logging.info("User Money Deposited Successfully")
        elif choice == 4:
            withdraw_money()
            logging.info("User Money Withdrawn Successfully")
        elif choice == 5:
            check_balance()
            logging.info("User Balance Checked Successfully")
        elif choice == 6:
            display_account_details()
            logging.info("User Account Details Displayed Successfully")
        elif choice == 7:
            transfer_money()
            logging.info("User Money Transferred Successfully")
        elif choice == 8:
            delete_account()
            logging.info("User Account Deleted Successfully")
        elif choice == 9:
            exit()
            logging.info("Program Exited Successfully")
    else:
        print("Invalid Choice , Only Numbers Allowed")
        logging.error("Invalid Choice , Only Numbers Allowed")

if __name__ == "__main__":
    main()