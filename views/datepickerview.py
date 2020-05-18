import datetime
from selenium.webdriver.common.by import By
from base.baseView import BaseView
from utilities.logger import logger
import logging


class datepickerview(BaseView):

    log = logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Date Picker
    _date_picker_title_xpath = "//XCUIElementTypeNavigationBar[@name='Date Picker']"
    _day_xpath = "//XCUIElementTypePickerWheel"
    _hour_xpath = "//XCUIElementTypePickerWheel[2]"
    _min_xpath = "//XCUIElementTypePickerWheel[3]"
    _meridium_xpath = "//XCUIElementTypePickerWheel[4]"

    def choose_tomorrow_for_date_picker(self, strHour="11", strMinute="30", strMeridium="PM"):
        tomorrow = self.getTomorrowsDate()

        day_picker = self.wait_for_element_to_be_clickable(locatorType=By.XPATH, locator=datepickerview._day_xpath)
        day_picker.send_keys(tomorrow)

        hour_picker = self.wait_for_element_to_be_clickable(locatorType=By.XPATH, locator=datepickerview._hour_xpath)
        hour_picker.send_keys(strHour)

        minute_picker = self.wait_for_element_to_be_clickable(locatorType=By.XPATH, locator=datepickerview._min_xpath)
        minute_picker.send_keys(strMinute)

        meridium_picker = self.wait_for_element_to_be_clickable(locatorType=By.XPATH, locator=datepickerview._meridium_xpath)
        meridium_picker.send_keys(strMeridium)

    def getTomorrowsDate(self):
        return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%b %d")

    def verifyDatePickerLabel(self, strHour="11", strMinute="30", strMeridium="PM"):
        tomorrow = self.getTomorrowsDate()
        _text_locator = "//XCUIElementTypeStaticText[contains(@name, '{0}, 2020 at {1}:{2} {3}')]"
        _text_label = _text_locator.format(tomorrow, strHour, strMinute, strMeridium)
        static_text_label = self.driver.find_element_by_xpath(_text_label)
        return static_text_label.is_displayed()
