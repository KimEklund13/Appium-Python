import unittest
from views.home.homeview import HomeView
from views.datepickerview import DatePickerView
from utilities.statusoftest import StatusOfTest
import pytest


@pytest.mark.usefixtures("create_driver")
class TestDatePicker(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, create_driver, get_platform):
        self.homeView = HomeView(self.driver)
        self.datePicker = DatePickerView(self.driver, self.platform)
        self.testStatus = StatusOfTest(self.driver)

    def setUp(self):
        self.homeView.navigate_to_date_pickers_screen()

    def test_date_picker(self):
        self.datePicker.choose_tomorrow_for_date_picker()

        result = self.datePicker.verifyDatePickerLabel()
        self.testStatus.assertionMark("test_date_picker", result, "Verifying date text label is displayed")
