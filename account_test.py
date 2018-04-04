import unittest #importing the unittest module
from account import Account #Importing the accountclass

class TestAccount(unittest.TestCase):
     """
     Test class that defines test cases for the contact class behaviours.
     Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     """

     def setUp(self):
         '''
         set up method run before each test cases.
         '''
         self.new_account = Account("Faith","Thuita","thuita15@gmail.com","egui") #create account object
     def test_init(self):
         '''
         test_init case to test if the object is initialized properly
         '''
         self.assertEqual(self.new_account.first_name,"Faith")
         self.assertEqual(self.new_account.last_name,"Thuita")
         self.assertEqual(self.new_account.email,"thuita15@gmail.com")
         self.assertEqual(self.new_account.password,"egui")

     def test_save_account(self):

         self.new_account.save_account() #saving the new account

         self.assertEqual(len(Account.account_list),1)
     def tearDown(self):
         Account.account_list = []

     def test_save_multiple_account(self):

         self.new_account.save_account()
         test_account = Account("mwangi","njuguna","mwangi12@gmail.com","press") #new account
         test_account.save_account()
         self.assertEqual(len(Account.account_list),2)
     def tearDown(self):
         Account.account_list = []

     def test_delete_account(self):
         self.new_account.save_account()
         test_account = Account("mwangi","njuguna","mwangi12@gmail.com","press")
         test_account.save_account()
         self.new_account.delete_account() #deleting account
         self.assertEqual(len(Account.account_list),1)
     def test_find_account_by_email(self):
         test_account = Account("mwangi","njuguna","mwangi12@gmail.com","press")
         test_account.save_account()
         found_account = Account.find_by_email("mwangi12@gmail.com")
         self.assertEqual(found_account.email,test_account.email)
     def test_account_exists(self):
         test2_account = Account("mwangi","njuguna","kamau@gmail.com","press")
         test2_account.save_account()

         account_exists = test2_account.account_exist("kamau@gmail.com")

         self.assertTrue(account_exists)
     def test_display_all_accounts(self):
         self.assertEqual(Account.display_accounts(),Account.account_list)
if __name__ == '__main__':
    unittest.main()
