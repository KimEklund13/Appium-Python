import datetime
from base.baseView import BaseView
from utilities.logger import logger
import logging


class DatePickerView(BaseView):

    log = logger(logging.DEBUG)

    def __init__(self, driver, platform):
        super().__init__(driver)
        self.driver = driver
        self.platform = platform

    # Locators
    def get_date_picker_title_locator(self):
        platform = self.platform.lower()
        _date_picker_title_xpath = ""
        try:
            if platform == "ios":
                _date_picker_title_xpath = "//XCUIElementTypeNavigationBar[@name='Date Picker']"
            elif platform == "android":
                _date_picker_title_xpath = ""
            return _date_picker_title_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'date picker title'")

    def get_day_wheel_locator(self):
        platform = self.platform.lower()
        _day_xpath = ""
        try:
            if platform == "ios":
                _day_xpath = "//XCUIElementTypePickerWheel"
            elif platform == "android":
                _day_xpath = ""
            return _day_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'day wheel'")

    def get_hour_wheel_locator(self):
        platform = self.platform.lower()
        _hour_xpath = ""
        try:
            if platform == "ios":
                _hour_xpath = "//XCUIElementTypePickerWheel[2]"
            elif platform == "android":
                _hour_xpath = ""
            return _hour_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'day wheel'")

    def get_minute_wheel_locator(self):
        platform = self.platform.lower()
        _min_xpath = ""
        try:
            if platform == "ios":
                _min_xpath = "//XCUIElementTypePickerWheel[3]"
            elif platform == "android":
                _min_xpath = ""
            return _min_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'day wheel'")

    def get_meridium_wheel_locator(self):
        platform = self.platform.lower()
        _meridium_xpath = ""
        try:
            if platform == "ios":
                _meridium_xpath = "//XCUIElementTypePickerWheel[4]"
            elif platform == "android":
                _meridium_xpath = ""
            return _meridium_xpath
        except:
            self.log.error("Platform not provided. Cannot get 'day wheel'")

    def choose_tomorrow_for_date_picker(self, strHour="11", strMinute="30", strMeridium="PM"):
        tomorrow = self.getTomorrowsDate()

        day_picker = self.get_element(self.get_day_wheel_locator(), "xpath")
        day_picker.send_keys(tomorrow)

        hour_picker = self.get_element(self.get_hour_wheel_locator(), "xpath")
        hour_picker.send_keys(strHour)

        minute_picker = self.get_element(self.get_minute_wheel_locator(), "xpath")
        minute_picker.send_keys(strMinute)

        meridium_picker = self.get_element(self.get_meridium_wheel_locator(), "xpath")
        meridium_picker.send_keys(strMeridium)

    def getTomorrowsDate(self):
        return (datetime.date.today() + datetime.timedelta(days=1)).strftime("%b %d")

    def verifyDatePickerLabel(self, strHour="11", strMinute="30", strMeridium="PM"):
        tomorrow = self.getTomorrowsDate()
        _text_locator = "//XCUIElementTypeStaticText[contains(@name, '{0}, 2020 at {1}:{2} {3}')]"
        _text_label = _text_locator.format(tomorrow, strHour, strMinute, strMeridium)
        static_text_label = self.get_element(_text_label, "xpath")
        # return static_text_label.is_displayed()
        return self.is_element_displayed(element=static_text_label)
