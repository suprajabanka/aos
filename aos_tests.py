import unittest
import aos_locators as locators
import aos_methods as methods


class aosappPositiveTestCases (unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setup()
        methods.create_new_user()
        methods.validate_new_user_is_created(locators.username)
        methods.log_out()
        methods.log_in(locators.username, locators.password)
        methods.validate_new_user_can_login(locators.username)
        methods.log_out()
        methods.tear_down()

