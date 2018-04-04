import unittest #Importing the unittest module
from profiles import Profiles # importing profiles class

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

if __name__ == '__main__':
    unittest.main()
