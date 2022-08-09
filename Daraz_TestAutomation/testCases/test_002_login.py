import pytest
import time
from selenium import webdriver
from pageObjects.logout import Logout
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_002_login:
    baseURL = ReadProperties.getApplicationURL()
    userphone = ReadProperties.getUserPhone()
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
        self.lp.clickToLoginPage()
        self.lp.setUserPhone(self.userphone)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)

        act_title = self.driver.title
        if act_title == "Online Shopping in Bangladesh: Order Now from Daraz.com.bd":
            self.logger.info("***** Login Test is Passed *****")
            assert True
            #logout
            self.logout = Logout(self.driver)
            self.logout.clickToUserAccount()
            time.sleep(3)
            self.logout.clickToLogout()
        else:
            self.logger.error("***** Login Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Daraz_TestAutomation\\screenshots\\test_002_login.png")
            self.driver.close()
            assert False

        self.driver.close()

        self.logger.info("***** End of Verifying Login Test *****")
        self.logger.info("***** Completed Test_002_login *****")

