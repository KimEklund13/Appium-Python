from utilities.statusoftest import StatusOfTest
from views.home.homeview import HomeView
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.homeView = HomeView(self.driver)
        self.testStatus = StatusOfTest(self.driver)

    def test_navigation_for_all_cells(self):

        self.homeView.navigate_to_each_view()

        result = self.homeView.assertUICatalogTitleExists()  # This is the assertion statement (true or false is returned)
        self.testStatus.assertionMark("test_navigation", result, "Verifying UI Catalog title exists")  # This method calls assert

    def test_whatever(self):
        pass
