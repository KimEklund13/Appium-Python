from base.baseView import BaseView
from utilities.logger import logger as logger
import logging


class HomeView(BaseView):

    log = logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assertUICatalogTitleExists(self):
        title = self.getUICatalogTitle()
        return title.is_displayed()

    def getUICatalogTitle(self):
        return self.waitForElementToAppear(locator=self._ui_catalog_xpath, locatorType="xpath")

    def navigate_to_each_view(self):
        elementList = self.driver.find_elements_by_xpath(".//XCUIElementTypeButton[@name='More Info']")
        clickCount = 0

        for cell in elementList:
            self.elementClick(element=cell)
            self.driver.back()
            self.waitForElementToAppear(locator=self._ui_catalog_xpath, locatorType="xpath")
            clickCount += 1

            if clickCount == 10:
                self.vertical_swipe_iOS("up")

    # Interactions
    def navigate_to_action_sheets_screen(self):
        self.elementClick(self._action_sheets_id)

    def navigate_to_activity_indicators_screen(self):
        self.elementClick(self._activity_indicators_id)

    def navigate_to_alert_views_screen(self):
        self.elementClick(self._alert_views_id)

    def navigate_to_buttons_screen(self):
        self.elementClick(self._buttons_id)

    def navigate_to_date_pickers_screen(self):
        self.elementClick(self._date_picker_id)

    def navigate_to_image_views_screen(self):
        self.elementClick(self._image_view_id)

    def navigate_to_page_controls_screen(self):
        self.elementClick(self._page_control_id)

    def navigate_to_picker_view_screen(self):
        self.elementClick(self._picker_view_id)

    def navigate_to_progress_views_screen(self):
        self.elementClick(self._progress_views_id)

    def navigate_to_segmented_controls_screen(self):
        self.elementClick(self._segmented_controls_id)

    def navigate_to_sliders_screen(self):
        self.elementClick(self._sliders_id)

    def navigate_to_steppers_screen(self):
        self.elementClick(self._sliders_id)

    def navigate_to_switches_screen(self):
        self.elementClick(self._switches_id)

    def navigate_to_text_fields_screen(self):
        self.elementClick(self._text_fields_id)

    def navigate_to_text_views_screen(self):
        self.elementClick(self._text_view_id)

    def navigate_to_web_view_screen(self):
        self.elementClick(self._web_view_id)

    def navigate_to_search_bars_screen(self):
        self.elementClick(self._search_bars_id)

    def navigate_to_tool_bars_screen(self):
        self.elementClick(self._toolbars_id)

    # Element Paths
    _ui_catalog_xpath = "//XCUIElementTypeNavigationBar[@name='UICatalog']"
    _action_sheets_id = "Action Sheets"
    _activity_indicators_id = "Activity Indicators"
    _alert_views_id = "Alert Views"
    _buttons_id = "Buttons"
    _date_picker_id = "Date Picker"
    _image_view_id = "Image View"
    _page_control_id = "Page Control"
    _picker_view_id = "Picker View"
    _progress_views_id = "Progress Views"
    _segmented_controls_id = "Segmented Controls"
    _sliders_id = "Sliders"
    _steppers_id = "Steppers"
    _switches_id = "Switches"
    _text_fields_id = "Text Fields"
    _text_view_id = "Text View"
    _web_view_id = "Web View"
    _search_bars_id = "Search Bars"
    _toolbars_id = "Toolbars"
