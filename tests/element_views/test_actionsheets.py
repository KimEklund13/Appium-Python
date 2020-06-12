from views.actionsheetsview import ActionSheetsView
from utilities.statusoftest import StatusOfTest
from views.home.homeview import HomeView
import unittest
import pytest


@pytest.mark.usefixtures("create_driver")
class ActionSheetsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, create_driver, get_platform):
        self.ASView = ActionSheetsView(self.driver, self.platform)
        self.testStatus = StatusOfTest(self.driver)
        self.homeView = HomeView(self.driver)

    def setUp(self):
        self.homeView.navigate_to_action_sheets_screen()

    def test_tapping_on_ok_cancel_button(self):
        self.ASView.click_ok_cancel_button()
        result = self.ASView.verify_buttons_appear()
        self.testStatus.verifyMark(result, "\nVerifying OK and Cancel buttons appear for 1st time")

        self.ASView.click_os_cancel_button()
        result = self.ASView.verify_buttons_disappear()
        self.testStatus.verifyMark(result,
                                   "\nVerifying OK and Cancel buttons are not displayed after clicking OS Cancel button")

        self.ASView.click_ok_cancel_button()
        result = self.ASView.verify_buttons_appear()
        self.testStatus.verifyMark(result, "\nVerifying OK and Cancel buttons appear for 2nd time")

        self.ASView.click_os_ok_button()
        result = self.ASView.verify_buttons_disappear()
        self.testStatus.assertionMark("test_tapping_on_ok_cancel_button", result,
                                      "\nVerifying OK and Cancel buttons are not displayed after clicking OS OK button")

    def test_whatever(self):
        pass

    def test_whatever2(self):
        pass

    def test_whatever3(self):
        pass
