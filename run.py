from account import Account
from profiles import Profiles

def create_account(fname,lname,email,password):
    new_account = Account(fname,lname,email,password)
    return new_account
def save_account(account):
    account.save_account()
def delete_account(account):
    account.delete_account()
def find_by_email(email):
    return account.find_by_email(email)
def check_existing_accounts(email):
    return Account.account_exist(email)
def display_accounts():
    return Account.display_accounts()

#Functions for the profiles class
def save_profiles(username,email,password):
    profiles.save_profiles()
def delete_profiles(profiles):
    profiles.delete_profiles()
def find_profiles_by_username(username):
    return profiles.find_profiles_by_username(username)
def checking_existing_profiles(username):
    return Profiles.profiles_exist(username)
def display_profiles():
    return Profiles.display_profiles()
def generate_password(password):
    return Profiles.generate_password()


def main():
        print("Hello, welcome to the password locker. Please enter your name")

        user_namep = input()
        print(f"Hello {user_namep}. do you have an account? if yes login, if no sign up"yes/no)

        print('\n')
        user_prompt = input().lower()
        if user_prompt == "no":
            print("Enter your first name")
            first_name = input()
            print("Enter your last name")
            last_name = input()
            print("Enter a valid email")
            email = input()
            print("Enter a password")
            password = input()
































        while True:
            print("Use these short codes: ca - create an account, da- display account, fa- find an account, ex- exit the account")

            short_code = input().lower()

            if short_code == 'ca':
                print("New Account")

                print("First name")
                f_name = input()

                print("Last name")
                l_name = input()

                print("email")
                email = input()

                print("Enter your password")
                password = input()
                save_accounts(create_account(f_name,l_name,email,password)) #create and save new account
                print('\n')
                print(f"New Account {f_name} {l_name} created")

                print('\n')
            #elif short_code == 'da':
if __name__ == '__main__':
    main()
