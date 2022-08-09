import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.logout import Logout
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_007_logout:
    baseURL = ReadProperties.getApplicationURL()
    email = ReadProperties.getEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, setup):
        self.logger.info("***** Starting Test_007_logout *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lwe = LoginPage(self.driver)
        time.sleep(5)
        self.lwe.clickToLogin()
        self.driver.implicitly_wait(50)
        self.lwe.clickContinuewithEmail()
        self.lwe.setEmail(self.email)
        self.lwe.setPassword(self.password)
        self.lwe.clickLogin()
        time.sleep(5)
        self.logger.info("***** Login Successfully *****")

        # logout
        self.lo = Logout(self.driver)
        self.lo.clicktoMyAccount()
        self.lo.clicktoSettings()
        self.lo.clicktoLogoutButton()
        self.logger.info("***** Logout Successfully *****")

        self.logger.info("***** End of Verifying Logout Test *****")
        self.logger.info("***** Completed Test_007_logout *****")