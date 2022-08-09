import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_002_loginwithEmail:
    baseURL = ReadProperties.getApplicationURL()
    email = ReadProperties.getEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginwithEmail(self, setup):
        self.logger.info("***** Starting Test_002_loginwithEmail *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("***** Verifying Login with Email Test *****")
        self.lwe = LoginPage(self.driver)
        time.sleep(5)
        self.lwe.clickToLogin()
        self.driver.implicitly_wait(50)
        self.lwe.clickContinuewithEmail()
        self.lwe.setEmail(self.email)
        self.lwe.setPassword(self.password)
        self.lwe.clickLogin()
        time.sleep(5)

        act_title = self.driver.title
        if act_title == "Bikroy.com - Electronics, Cars, Property and Jobs in Bangladesh":
            self.logger.info("***** Login with Email Test is Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Login with Email Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Bikroy.com_TestAutomation\\screenshots\\test_002_loginwithEmail.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Verifying Login with Email Test *****")
        self.logger.info("***** Completed Test_002_loginwithEmail *****")