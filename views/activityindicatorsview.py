from base.baseView import BaseView
from utilities.logger import logger
import logging
from selenium.common.exceptions import NoSuchElementException


class ActivityIndicators(BaseView):
    log = logger(logging.DEBUG)

    def __init__(self, driver, platform):
        super().__init__(driver)
        self.driver = driver
        self.platform = platform

    # Locators
    # Should I just refactor these to be tuples and unpack them in the 'get' methods?
    # If I do that, I should clean up the AppiumDriver class to also use and unpack tuples

    def get_activity_indicator_title_locator(self):
        platform = self.platform.lower()
        _activity_indicator_title_xpath = ""
        try:
            if platform == "ios":
                _activity_indicator_title_xpath = "//XCUIElementTypeNavigationBar[@name='Activity Indicators']"
            elif platform == "android":
                _activity_indicator_title_xpath = ""
            return _activity_indicator_title_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'activity indicator title'")

    def get_gray_spinner_locator(self):
        platform = self.platform.lower()
        _gray_spinner_xpath = ""
        try:
            if platform == "ios":
                _gray_spinner_xpath = "(//XCUIElementTypeActivityIndicator[@name='In progress'])[1]"
            elif platform == "android":
                _gray_spinner_xpath = ""
            return _gray_spinner_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'gray spinner'")

    def get_tinted_spinner_locator(self):
        platform = self.platform.lower()
        _tinted_spinner_xpath = ""
        try:
            if platform == "ios":
                _tinted_spinner_xpath = "(//XCUIElementTypeActivityIndicator[@name='In progress])[2]"
            elif platform == "android":
                _tinted_spinner_xpath = ""
            return _tinted_spinner_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'gray spinner'")

    def get_gray_label_locator(self):
        platform = self.platform.lower()
        _gray_label_xpath = ""
        try:
            if platform == "ios":
                _gray_label_xpath = "(//XCUIElementTypeOther[@name='GRAY'])[1]"
            elif platform == "android":
                _gray_label_xpath = ""
            return _gray_label_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'gray label'")

    def get_tinted_label_locator(self):
        platform = self.platform.lower()
        _tinted_label_xpath = ""
        try:
            if platform == "ios":
                _tinted_label_xpath = "(//XCUIElementTypeOther[@name='TINTED'])[1]"
            elif platform == "android":
                _tinted_label_xpath = ""
            return _tinted_label_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'gray label'")

    # Methods
    def activity_indicators_title_is_displayed(self):
        activity_indicators_title = self.get_activity_indicator_title_locator()
        return self.is_element_present(activity_indicators_title, "xpath")

