import unittest #Importing the unittest module
from profiles import Profiles # importing profiles class
import pyperclip

class TestProfiles(unittest.TestCase):

     def setUp(self):
         self.new_profiles = Profiles("thuitafaith","thuita12@gmail.com","prrr")

     def test_init(self):
         self.assertEqual(self.new_profiles.username,"thuitafaith")
         self.assertEqual(self.new_profiles.email,"thuita12@gmail.com")
         self.assertEqual(self.new_profiles.password,"prrr")
     def test_save_profiles(self):
         self.new_profiles.save_profiles() #saving the new profile
         self.assertEqual(len(Profiles.profiles_list),1)
     def tearDown(self):
         Profiles.profiles_list = []

     def test_save_multiple_profiles(self):
         self.new_profiles.save_profiles()
         test_profiles = Profiles("tinakathambi","tina13@gmail.com","skrrr") # new profile
         test_profiles.save_profiles()
         self.assertEqual(len(Profiles.profiles_list),2)
     def test_delete_profiles(self):
         self.new_profiles.save_profiles()
         test_profiles = Profiles("tinakathambi","tina13@gmail.com","skrrr")
         test_profiles.save_profiles()
         self.new_profiles.delete_profiles()
         self.assertEqual(len(Profiles.profiles_list),1)
     def test_find_profiles_by_username(self):
         self.new_profiles.save_profiles()
         test_profiles = Profiles("tinakathambi","tina13@gmail.com","skrrr")
         test_profiles.save_profiles()
         found_profiles = Profiles.find_by_username("tinakathambi")
         self.assertEqual(found_profiles.username,test_profiles.username)
     def tearDown(self):
         Profiles.profiles_list = []
     def test_profiles_exists(self):
         self.new_profiles.save_profiles()
         test_profiles = Profiles("thuitafaith","thuita12@gmail.com","prrr")
         test_profiles.save_profiles()
         profiles_exists = Profiles.profiles_exist("thuitafaith")
         self.assertTrue(profiles_exists)
     def test_display_all_profiles(self):
         self.assertEqual(Profiles.display_profiles(),Profiles.profiles_list)
     def test_generate_password(self):
         test_profiles = Profiles("thuitafaith","thuita12@gmail.com","prrr")
         test_profiles.save_profiles()
         password_changed = test_profiles.generate_password("thuitafaith",8)
         self.assertTrue(len(test_profiles.password),8)
     def test_copy_password(self):
         test_profiles = Profiles("thuitafaith","thuita12@gmail.com","prrr")
         test_profiles.save_profiles()
         test_profiles.generate_password("thuitafaith",9)
         Profiles.copy_password("thuitafaith")
         self.assertEqual(test_profiles.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
