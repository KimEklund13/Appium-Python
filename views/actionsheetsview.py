from base.baseView import BaseView
from utilities.logger import logger
import logging


class ActionSheetsView(BaseView):
    log = logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Action Sheets
    _action_sheets_title_xpath = "//XCUIElementTypeNavigationBar[@name='Action Sheets']"
    _ok_cancel_id = "Okay / Cancel"
    _other_id = "Other"
    _os_ok_button_id = "OK"
    _os_cancel_button_id = "Cancel"

    # Create interaction methods for each element
    def click_ok_cancel_button(self):
        self.click_element(self._ok_cancel_id)

    def click_other_button(self):
        self.click_element(self._other_id)

    def click_os_ok_button(self):
        self.click_element(self._os_ok_button_id)

    def click_os_cancel_button(self):
        self.click_element(self._os_cancel_button_id)

    # Verifications/Assertions
    def verify_buttons_disappear(self):
        return not self.element_list_presence(".//XCUIElementTypeSheet//XCUIElementTypeButton", locator_type="xpath")

    def verify_buttons_appear(self):
        return self.element_list_presence(".//XCUIElementTypeSheet//XCUIElementTypeButton", locator_type="xpath")

