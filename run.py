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
def create_profile(fname,lname,password):
    new_account = Profiles(fname,lname,password)
    return new_account
def save_profiles(profiles):
    profiles.save_profiles()
def delete_profiles(profiles):
    profiles.delete_profiles()
def find_profiles_by_username(username):
    return Profiles.find_by_username(username)
def checking_existing_profiles(username):
    return Profiles.profiles_exist(username)
def display_profiles():
    return Profiles.display_profiles()
def generate_password(username,password):
    return Profiles.generate_password(username,password)
def copy_profile_password(username):
    return Profiles.copy_password(username)

def Profile_():
    while True:
        print("Use these short codes: cp - create profile, dp- display profile, fp- find a profile,gp-generate password, ex- exit the profile")

        short_code = input().lower()

        if short_code == 'cp':
            print("\t\t New Profiles")

            print("Enter profile name")
            profile_name = input()

            print("Enter your email")
            email = input()

            print("Enter your password")
            password = input()

            if profile_name == "" or email == "" or password == "":
                print("You can not submit empty fields")


            else:
                if checking_existing_profiles(profile_name):
                    print("Profile already exists")
                else:
                    n_prof = create_profile(profile_name,email,password)
                    save_profiles(n_prof) #create and save new account
                    print('\n')
                    print(f"New Profile {profile_name} {email} {password} created")
                    print('\n')
        elif short_code == 'dp':
            if display_profiles():
                print("Here is your profile")
                print('\n')
                for profile in display_profiles():
                    print(f"PROFILE NAME : {profile.username} \n PROFILE EMAIL: {profile.email} \n PROFILE PASSWORD: {profile.password}")
            else:
                print('\n')
                print("There is no profile available")
        elif short_code == 'fp':
            print("Enter the user name for the profile you want to look for")
            search_username = input()
            profile_found = checking_existing_profiles(search_username)
            if profile_found:
                user_find = find_profiles_by_username(search_username)
                print(f"PROFILE NAME : {user_find.username} \n PROFILE EMAIL: {user_find.email} \n PROFILE PASSWORD: {user_find.password}")
                print(f"{search_username}")
            else:
                print("\n")
                print("Profile not found")
                print("\n")

        elif short_code == 'gp':
            print("Enter the username for which you want to change password")
            username_change_pass = input()
            print("Enter the length of the password you want")
            password_length = input()
            if username_change_pass == "" or password_length=="":
                print("You cannot submit an empty field(s)")
            else:
                profile_found = checking_existing_profiles(username_change_pass)
                if not profile_found:
                    print("No profile found")
                else:
                    try:
                        password_len = int(password_length)
                        if password_length.isdigit():
                            generate_password(username_change_pass,password_len)
                        else:
                            print("Negative numbers not allowed")
                    except ValueError:
                        print("Only numbers are allowed")

        elif short_code == "copy":
            print("Enter the username of the profile you want to copy the password")
            copy_username = input()
            if copy_username=="":
                print("You must enter a profile name")
            else:
                profile_found = checking_existing_profiles(copy_username)
                if not profile_found:
                    print("No profile found")
                else:
                    if copy_profile_password(copy_username):
                        print("Password Copied!")

        elif short_code == 'ex':
            break
        else:
            print("Unrecognised command!Try again")





def main():
    print("Hello, welcome to the password locker. Please enter your name")
    user_namep = input()
    while True:


        print(f"Hello {user_namep}. do you have an account? if yes login, if no sign up?yes/no")


        user_prompt = input().lower().replace(" ","")
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
