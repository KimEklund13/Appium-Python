"""
Base View class implementation
It implements methods which are common to all the pages throughout the app

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""

from base.appiumDriver import AppiumDriver
from traceback import print_stack
from utilities.util import Util


class BaseView(AppiumDriver):

    def __init__(self, driver):
        """
        Inits BaseView class
        """
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # This is only for web testing, there is no title in mobile
    def verifyPageTitle(self, titleToVerify):
        """
        Verify the view title
        :param titleToVerify: Title on the view that needs to be verified
        """
        try:
            actualTitle = self.get_web_title()
            return self.util.verify_text_contains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get the view title")
            print_stack()
            return False