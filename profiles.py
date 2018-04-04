class Profiles:
    '''
    create instances of class Profiles
    '''
    profiles_list = [] #Empty profiles profiles_list
    def save_profiles(self):
        Profiles.profiles_list.append(self)
    def delete_profiles(self):
        Profiles.profiles_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        for profiles in cls.profiles_list:
            if profiles.username == username:
                return profiles
    @classmethod
    def profiles_exist(cls,username):
        for profiles in cls.profiles_list:
            if profiles.username == username:
                return True
            else:
                return False
    def __init__(self,username,email,password = None):

        self.username = username
        self.email = email
        self.password = password
