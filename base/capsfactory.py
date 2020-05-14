"""
@package base

Capabilities Factory class implementation
It creates a webdriver instance based on device configurations

Example:
    cf = CapsFactory(device)
    cf.getDriverInstance
"""


from appium import webdriver


class CapsFactory:

    def __init__(self, device):
        """
        Inits CapsFactory class
        Returns:
            None
        """
        self.device = device

    """
    Set driver and platform environment based on OS
    
    XCUIDriver "/Users/KimEklund/XCUIDriver.exe"
    os.environ["XCUIDriver.iOS.driver"] = xcuidriver
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub')
    
    Preferred: Set the path on the machine where the tests will be executed
    """

    def getDriverInstance(self):

        remote_url = 'http://localhost:4723/wd/hub'

        # Seeing if i can create a CLI map for the appium CLI to generate this dictionary
        # But keep this file for running tests locally without CLI
        # This app doesn't have an android apk, but just putting stuff here to use on another app.

        if self.device == "android-sim":
            # Set android driver (espresso or uiautomator)
            # TODO Add caps for Android sim
            android_caps = {'platformVersion': '', 'platformName': '', 'deviceName': '',
                            'automationName': ''}
            driver = webdriver.Remote(remote_url, android_caps)
            print("Running tests on Android Simulator")
        elif self.device == "ios-real-device":
            # Set XCUIDriver
            # TODO Add caps for iOS real device
            physical_ios_caps = {'platformVersion': '12.4', 'platformName': 'iOS', 'deviceName': 'iPhone 8 Plus',
                                 'automationName': 'XCUITest', 'bundleId': 'com.example.apple-samplecode.UICatalog',
                                 'uuid': '', 'xcodeOrgId': '', 'xcodeSigningId': ''}
            driver = webdriver.Remote(remote_url, physical_ios_caps)
            print("Running tests on iOS Physical Device")
        elif self.device == "android-real-device":
            # Set android driver (espresso or uiautomator)
            # TODO Add caps for Android real device
            physical_android_caps = {'platformVersion': '', 'platformName': '', 'deviceName': '',
                                     'automationName': '', 'bundleId': ''}
            driver = webdriver.Remote(remote_url, physical_android_caps)
            print("Running tests on iOS Physical Device")
        else:
            # Set XCUIDriver driver
            ios_caps = {'platformVersion': '12.4', 'platformName': 'iOS', 'deviceName': 'iPhone 8 Plus',
                        'automationName': 'XCUITest', 'bundleId': 'com.example.apple-samplecode.UICatalog'}
            driver = webdriver.Remote(remote_url, ios_caps)
            print("Running tests on iOS Simulator")

        driver.implicitly_wait(3)
        return driver
