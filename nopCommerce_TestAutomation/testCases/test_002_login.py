import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_002_login:
    baseURL = ReadProperties.getApplicationURL()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***** Starting Test_002_login *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("***** Verifying Login Test *****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("***** Login Test is Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Login Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\nopCommerce_TestAutomation\\screenshots\\test_002_login.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Verifying Login Test *****")
        self.logger.info("***** Completed Test_002_login *****")

