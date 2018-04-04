import unittest #Importing the unittest module
from profiles import Profiles # importing profiles class

class TestProfiles(unittest.TestCase):

     def setUp(self):
         self.new_profiles = Profiles("thuitafaith","thuita12@gmail.com","prrr")

     def test_init(self):
         self.assertEqual(self.new_profiles.username,"thuitafaith")
         self.assertEqual(self.new_profiles.email,"thuita12@gmail.com")
         self.assertEqual(self.new_profiles.password,"prrr")

if __name__ == '__main__':
    unittest.main()
