from base.baseView import BaseView
from utilities.logger import logger
import logging


# noinspection PyBroadException
class ActionSheetsView(BaseView):
    log = logger(logging.DEBUG)

    def __init__(self, driver, platform):
        super().__init__(driver)
        self.driver = driver
        self.platform = platform

    # Locators
    def get_action_sheets_title_locator(self):
        platform = self.platform.lower()
        _action_sheets_title_xpath = ""
        try:
            if platform == "ios":
                _action_sheets_title_xpath = "//XCUIElementTypeNavigationBar[@name='Action Sheets']"
            elif platform == "android":
                _action_sheets_title_xpath = ""
            return _action_sheets_title_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'action sheets title'")

    def get_ok_cancel_locator(self):
        platform = self.platform.lower()
        _ok_cancel_id = ""
        try:
            if platform == "ios":
                _ok_cancel_id = "Okay / Cancel"
            elif platform == "android":
                _ok_cancel_id = ""
            return _ok_cancel_id
        except:
            self.log.error("Platform not provided. Cannot get 'Okay/Cancel button'")

    def get_other_locator(self):
        platform = self.platform.lower()
        _other_id = ""
        try:
            if platform == "ios":
                _other_id = "Other"
            elif platform == "android":
                _other_id = ""
            return _other_id
        except:
            self.log.error("Platform not provided. Cannot get 'Other button'")

    def get_ok_locator(self):
        platform = self.platform.lower()
        _os_ok_button_id = ""
        try:
            if platform == "ios":
                _os_ok_button_id = "OK"
            elif platform == "android":
                _os_ok_button_id = ""
            return _os_ok_button_id
        except:
            self.log.error("Platform not provided. Cannot get 'OS 'ok' button'")

    def get_cancel_locator(self):
        platform = self.platform.lower()
        _os_cancel_button_id = ""
        try:
            if platform == "ios":
                _os_cancel_button_id = "Cancel"
            elif platform == "android":
                _os_cancel_button_id = ""
            return _os_cancel_button_id
        except:
            self.log.error("Platform not provided. Cannot get 'OS 'cancel' button'")

    # Interactions
    def click_ok_cancel_button(self):
        self.click_element(self.get_ok_cancel_locator())

    def click_other_button(self):
        self.click_element(self.get_other_locator())

    def click_os_ok_button(self):
        self.click_element(self.get_ok_locator())

    def click_os_cancel_button(self):
        self.click_element(self.get_cancel_locator())

    # Verifications/Assertions
    def verify_buttons_disappear(self):
        return not self.element_list_presence(".//XCUIElementTypeSheet//XCUIElementTypeButton", locator_type="xpath")

    def verify_buttons_appear(self):
        return self.element_list_presence(".//XCUIElementTypeSheet//XCUIElementTypeButton", locator_type="xpath")

