"""
@package base

Capabilities Factory class implementation
It creates a webdriver instance based on device configurations

Example:
    cf = CapsFactory(device)
    cf.getDriverInstance
"""

from utilities.logger import logger
import logging
from appium import webdriver


class CapsFactory:
    log = logger(logging.DEBUG)

    def __init__(self, device):
        self.device = device

    """
    Set driver and platform environment based on OS
    
    XCUIDriver "/Users/KimEklund/XCUIDriver.exe"
    os.environ["XCUIDriver.iOS.driver"] = xcuidriver
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub')
    
    Preferred: Set the path on the machine where the tests will be executed
    """

    def get_driver_instance(self):

        remote_url = 'http://localhost:4723/wd/hub'
        caps = self.get_capabilities()

        driver = webdriver.Remote(remote_url, caps)
        driver.implicitly_wait(3)
        return driver

    def get_platform_name(self):
        platformName = self.get_capabilities()['platformName']
        return platformName

    def get_capabilities(self):
        try:
            if self.device == "android-sim":
                # Set android driver (espresso or uiautomator)
                # TODO Add caps for Android sim
                caps = {'platformVersion': '', 'platformName': 'Android', 'deviceName': '',
                        'automationName': '', 'app': ''}
            elif self.device == "ios-real-device":
                # Set XCUIDriver
                # TODO Add caps for iOS real device
                caps = {'platformVersion': '12.4', 'platformName': 'iOS', 'deviceName': 'iPhone 8 Plus',
                        'automationName': 'XCUITest', 'bundleId': 'com.example.apple-samplecode.UICatalog',
                        'uuid': '', 'xcodeOrgId': '', 'xcodeSigningId': ''}
                self.log.info("Running tests on iOS Physical Device")
            elif self.device == "android-real-device":
                # Set android driver (espresso or uiautomator)
                # TODO Add caps for Android real device
                caps = {'platformVersion': '', 'platformName': 'Android', 'deviceName': '',
                        'automationName': '', 'app': ''}
                self.log.info("Running tests on iOS Physical Device")
            else:
                # Set XCUIDriver driver
                caps = {'platformVersion': '12.4', 'platformName': 'iOS', 'deviceName': 'iPhone 8 Plus',
                        'automationName': 'XCUITest', 'bundleId': 'com.example.apple-samplecode.UICatalog'}
                self.log.info("Running tests on iOS Simulator")
            return caps
        except:
            self.log.error("Could not return desired capabilities")

