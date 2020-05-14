import time
import os
from traceback import print_stack
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from utilities.logger import logger
import logging


# noinspection PyBroadException
class AppiumDriver:
    log = logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getWebTitle(self):
        """
        Used for web testing, if app opens Safari/Chrome?
        """
        return self.driver.title

    def screenShot(self, resultMessage):
        """
        Takes a screenshot of the current open view
        Called normally upon test failure
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenShotDirectory = "../screenshots/"
        relativeFileName = screenShotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)  # gets current file and dir of current file
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def vertical_swipe_iOS(self, direction):
        """
        Swipes the app in the direction passed in.
        Does not scroll to determined coordinates
        :param direction: "up" or "down"
        """
        self.driver.execute_script("mobile: swipe", {"direction": direction})

    def waitForElementToBeClickable(self, locator, locatorType="id",
                                    timeout=10, pollFrequency=0.5):
        """
        Waits for an element based on expected conditions (to be clickable)
        :param locator: Locator string (Ex: "id_name")
        :param locatorType: See 'getByType' for arguments (Ex: "accessibilityid"
        :param timeout: Int in seconds
        :param pollFrequency: Int in seconds
        :return: returns clickable element once the element is clickable if timeout does not expire
        """
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def getByType(self, locatorType):
        """
        Takes a short-hand string and returns the By.LOCATORTYPE
        :param locatorType: String
        :return: By.LOCATORTYPE
        """
        locatorType = locatorType.lower()
        if locatorType == "accessibilityid":
            # iOS: accessibility-id
            # Android: content-desc
            return MobileBy.ACCESSIBILITY_ID
        elif locatorType == "classname":
            # iOS: full name of the XCUI element and begins with XCUIElementType
            # Android: full name of the UIAutomator2 class (e.g.: android.widget.TextView)
            return By.CLASS_NAME
        elif locatorType == "id":
            # Native element identifier. resource-id for android; name for iOS.
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "image":
            return MobileBy.IMAGE
        elif locatorType == "uiautomator":
            # UIAutomator2 only
            return MobileBy.ANDROID_UIAUTOMATOR
        elif locatorType == "viewtag":
            # Espresso only
            return MobileBy.ANDROID_VIEWTAG
        elif locatorType == "datamatcher":
            # Espresso only
            return MobileBy.ANDROID_DATA_MATCHER
        elif locatorType == "classchain":
            # iOS only
            return MobileBy.IOS_CLASS_CHAIN
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.error("Locator type not supported - or check the argument you passed in")
        return False

    def getElement(self, locator, locatorType="accessibilityid"):
        """
        Queries for an element
        :param locator: Locator string (Ex: "id_name")
        :param locatorType: See 'getByType' for arguments (Ex: "accessibilityid")
        :return: element
        """
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and locator type: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="accessibilityid"):
        """
        Queries for a list of elements
        :param locator: Locator string (Ex: "id_name")
        :param locatorType: See 'getByType' for arguments (Ex: "accessibilityid")
        :return: element list
        """
        elementList = None
        try:
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) == 1:
                self.log.info("Only one element in list. Consider using the singular `getElement` method instead")
            self.log.info("Element list found")
        except:
            self.log.error("Element list not found")
        return elementList

    def elementClick(self, locator="", locatorType="accessibilityid", element=None):
        """
        Clicks on an element
        :param locator: Locator string (Ex: "id_name")
        :param locatorType: See 'getByType' for arguments (Ex: "accessibilityid")
        :param element: accepts an element in lieu of providing the locator and locatorType
        :return: click action on the element
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.error("Cannot click on the element with " + locator + " and locator type: " + locatorType)
            print_stack()

    def sendKeys(self, text, locator="", locatorType="accessibilityid", element=None):
        """
        Sends text to an element
        :param text: Text to be sent to the element
        :param locator: Locator string (Ex: "id_name")
        :param locatorType: See 'getByType' for arguments (Ex: "accessibilityid")
        :param element: accepts an element in lieu of providing the locator and locatorType
        :return: sends text to the element
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(text)
            self.log.info("Sent keys to element with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.error(
                "Cannot send keys to element with locator: " + locator + " and locator type: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="accessibilityid", element=None, info=""):
        """
        Get 'Text' from an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def clearField(self, locator="", locatorType="accessibilityid", element=None):
        """
        Clear an element field
        """
        if locator:
            element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def isElementPresent(self, locator="", locatorType="accessibilityid", element=None):
        """
        Checks for the presence of an element and returns a bool value.
        :param locator: Locator string (Ex: "id_name")
        :param locatorType: See 'getByType' for arguments (Ex: "accessibilityid")
        :param element: accepts an element in lieu of providing the locator and locatorType
        :return: True or False
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element is present")
                return True
            else:
                return False
        except:
            self.log.info("Element is not present")
            return False

    def elementListPresence(self, locator, locatorType="accessibilityid"):
        # plural elements, returns bool like isElementPresent()
        try:
            elementsList = self.getElementList(locator, locatorType)
            if len(elementsList) > 0:
                self.log.info("\nAt least one element in the list was found")
                return True
            else:
                return False
        except:
            self.log.info("\nElement(s) are not present")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    # TODO: Modify this for mobile context
    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def isDisabled(self, locator, locatorType="id", info=""):
        enabled = self.isEnabled(locator, locatorType, info)
        return not enabled  # Opposite of enabled
