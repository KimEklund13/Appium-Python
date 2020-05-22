from views.home.homeview import HomeView
from views.datepickerview import datepickerview
from utilities.statusoftest import StatusOfTest
import pytest


# TODO: This needs to be cleaned up and use a fixture and setup method for navigation
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestDatePicker:

    # @pytest.fixture(autouse=True)
    # def classSetup(self, oneTimeSetUp):
    #     self.homeView = HomeView(self.driver)
    #     self.testStatus = StatusOfTest(self.driver)

    def test_date_picker(self):
        home = HomeView(self.driver)
        datePicker = datepickerview(self.driver)
        testStatus = StatusOfTest(self.driver)

        # ----- actual test ------- #

        home.navigate_to_date_pickers_screen()

        datePicker.choose_tomorrow_for_date_picker()

        result = datePicker.verifyDatePickerLabel()
        testStatus.assertionMark("test_date_picker", result, "Verifying date text label is displayed")
