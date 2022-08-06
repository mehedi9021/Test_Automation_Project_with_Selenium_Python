import pytest
from selenium import webdriver
from pageObjects.logout import Logout
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_007_logout:
    baseURL = ReadProperties.getApplicationURL()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, setup):
        self.logger.info("***** Starting Test_007_logout *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Succesful *****")

        self.logger.info("***** Starting Logout Test *****")
        self.logout = Logout(self.driver)
        self.logout.clickLogout()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("***** Logout Test is Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Logout Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\nopCommerce_TestAutomation\\screenshots\\test_007_logout.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Logout Test *****")
        self.logger.info("***** Completed  Test_007_logout *****")