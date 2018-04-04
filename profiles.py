class Profiles:
    '''
    create instances of class Profiles
    '''
    profiles_list = [] #Empty profiles profiles_list
    def save_profiles(self):
        Profiles.profiles_list.append(self)
    def __init__(self,username,email,password = None):

        self.username = username
        self.email = email
        self.password = password
