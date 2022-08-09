import pytest
from selenium import webdriver
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_001_homePageTitle:
    baseURL = ReadProperties.getApplicationURL()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("***** Starting Test_001_homePageTitle *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("***** Verifying Home Page Title *****")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("***** Home Page Title Test is Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Home Page Title Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\nopCommerce_TestAutomation\\screenshots\\test_001_homePageTitle.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Verifying Home Page Title *****")
        self.logger.info("***** Completed Test_001_homePageTitle *****")