import unittest
import aos_locators as locators
import aos_methods as methods

class aoswebsitePositiveTestCases (unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.create_new_account()
        methods.sign_out()
        methods.validate_homepage_texts()
        methods.validate_contact_us()
        methods.validate_follow_us_links()
        methods.log_in()
        methods.delete_user()
        methods.tear_Down()


