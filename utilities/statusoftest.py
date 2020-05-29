import logging
from traceback import print_stack
from utilities.logger import logger
from base.appiumDriver import AppiumDriver


class StatusOfTest(AppiumDriver):
    log = logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCEEDED" + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED" + resultMessage)
                    self.take_screenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED - RESULT IS NONE" + resultMessage)
                self.take_screenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED ###")
            self.take_screenshot(resultMessage)
            print_stack()

    def verifyMark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case.
        Will not stop a test if there is a failure, but it will fail the test.
        """
        self.setResult(result, resultMessage)

    def assertionMark(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case (hard assertion)
        This will stop a test if it fails.
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED: ")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL: ")
            self.resultList.clear()
            assert True == True
