from utilities.statusoftest import StatusOfTest
from views.home.homeview import HomeView
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestHomePage:

    # @pytest.fixture(autouse=True)
    # def classSetup(self, oneTimeSetUp):
    #     self.homeView = HomeView(self.driver)
    #     self.testStatus = StatusOfTest(self.driver)

    def test_navigation(self):

        # Creating instances
        homeView = HomeView(self.driver)
        testStatus = StatusOfTest(self.driver)
        driver = self.driver

        # ---- actual test ---- #
        homeView.navigate_to_action_sheets_screen()
        driver.back()

        homeView.navigate_to_activity_indicators_screen()
        driver.back()

        homeView.navigate_to_alert_views_screen()
        driver.back()

        homeView.navigate_to_buttons_screen()
        driver.back()

        homeView.navigate_to_date_pickers_screen()
        driver.back()

        homeView.navigate_to_image_views_screen()
        driver.back()

        homeView.navigate_to_page_controls_screen()
        driver.back()

        homeView.navigate_to_picker_view_screen()
        driver.back()

        homeView.navigate_to_progress_views_screen()
        driver.back()

        homeView.navigate_to_segmented_controls_screen()
        driver.back()

        homeView.navigate_to_sliders_screen()
        driver.back()

        homeView.navigate_to_steppers_screen()
        driver.back()

        homeView.vertical_swipe_iOS("up")

        homeView.navigate_to_switches_screen()
        driver.back()

        homeView.navigate_to_text_fields_screen()
        driver.back()

        homeView.navigate_to_text_views_screen()
        driver.back()

        homeView.navigate_to_web_view_screen()
        driver.back()

        homeView.navigate_to_search_bars_screen()
        driver.back()

        homeView.navigate_to_tool_bars_screen()
        driver.back()

        result = homeView.assertUICatalogTitleExists()  # This is the assertion statement (true or false is returned)
        testStatus.assertionMark("test_navigation", result, "Verifying UI Catalog title exists")  # This method calls assert

    def test_whatever(self):
        pass
