from utilities.statusoftest import StatusOfTest
from views.home.homeview import HomeView
import pytest
import unittest


@pytest.mark.usefixtures("create_driver")
class TestHomePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, create_driver):
        self.homeView = HomeView(self.driver)
        self.testStatus = StatusOfTest(self.driver)

    def test_navigation_for_all_cells(self):

        self.homeView.navigate_to_each_view()

        result = self.homeView.assert_ui_catalog_title_exists()  # This is the assertion statement (true or false is returned)
        self.testStatus.assertionMark("test_navigation_for_all_cells", result, "Verifying UI Catalog title exists")  # This method calls assert

    def test_whatever(self):
        pass
