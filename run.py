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
def user_login(email,password):
    return Account.user_login(email,password)

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


def Profile_():
    while True:
        print("Use these short codes: cp - create profile, dp- display profile, fp- find a profile, ex- exit the profile")

        short_code = input().lower()

        if short_code == 'ca':
            print("New Profiles")

            print("Enter profile name")
            profile_name = input()

            print("Enter your email")
            email = input()

            print("Enter your password")
            password = input()

            save_profiles(create_profile(profile_name,email,password)) #create and save new account
            print('\n')
            print(f"New Profile {profile_name} {email} {password} created")

            print('\n')
        elif short_code == 'dp':
            if display_profiles():
                print("Here is your profile")
                print('\n')
                for profile in display_profiles():
                    print(f"{profile.profile_name} {profile.email} {profile.password}")
            else:
                print('\n')
                print("There is no such profile")
        elif short_code == 'fp':
            if find_profiles_by_username():
                print("Enter the user name for the profile you want to look for")
                search_username = input()

                if checking_existing_profiles(search_username)
                print(f"{search_username}")
            else:
                print("Profile not found")



        elif short_code == 'ex':
            print("Nice time")
        else:
            print("Try again")





def main():
    while True:
        print("Hello, welcome to the password locker. Please enter your name")

        user_namep = input()
        print(f"Hello {user_namep}. do you have an account? if yes login, if no sign up?yes/no")


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
            if first_name == ""or last_name == "" or email == "" or password == "":
                print("Error!you submitted empty field(s)")
            else:
                new_account = create_account(first_name,last_name,email,password)
                save_account(new_account)
                Profile_()

        elif user_prompt == "yes":
            print("Enter your email")
            user_email = input()
            print("Enter your password")
            user_password = input()
            if user_email == "" or user_password == "":
                print("Error!please enter the empty field(s)")
            else:
                user_found = user_login(user_email,user_password)
                if user_found:
                    Profile_()
                else:
                    print("enter correct credentials")
        else:
            print("What are you doing")




























if __name__ == '__main__':
    main()
