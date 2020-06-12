from utilities.statusoftest import StatusOfTest
from views.activityindicatorsview import ActivityIndicators
from views.home.homeview import HomeView
import pytest
import unittest


@pytest.mark.usefixtures("create_driver")
class ActivityIndicatorsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, create_driver, get_platform):
        self.ai = ActivityIndicators(self.driver, self.platform)
        self.testStatus = StatusOfTest(self.driver)
        self.homeView = HomeView(self.driver)

    def setUp(self):
        self.homeView.navigate_to_activity_indicators_screen()

    def test_activity_indicators_view_title_is_displayed(self):
        result = self.ai.activity_indicators_title_is_displayed()
        self.testStatus.assertionMark("test_activity_indicators_view_title_is_displayed",
                                      result, " ::: Verifying Activity Indicators View is displayed")

    def test_all_elements_are_displayed(self):
        result = self.ai.activity_all_elements_are_displayed()
        self.testStatus.assertionMark("test_all_elements_are_displayed", result,
                                      " ::: Verifying all elements on Activity Indicators are displayed")
