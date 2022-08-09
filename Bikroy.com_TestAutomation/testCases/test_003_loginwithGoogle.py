import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_003_loginwithGoogle:
    baseURL = ReadProperties.getApplicationURL()
    email = ReadProperties.getEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginwithGoogle(self, setup):
        self.logger.info("***** Starting Test_003_loginwithGoogle *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("***** Verifying Login with Google Test *****")
        self.lwg = LoginPage(self.driver)
        time.sleep(5)
        self.lwg.clickToLogin()
        self.driver.implicitly_wait(50)
        self.lwg.clickContinuewitGoogle()
        self.lwg.setTestEmail("mr.tester.9021@gmail.com")
        time.sleep(5)
        self.lwg.clicktoEmailNext()
        time.sleep(5)
        self.lwg.setTestPassword("@Tester1234")
        time.sleep(5)
        self.lwg.clicktoPasswordNext()
        time.sleep(5)

        act_title = self.driver.title
        if act_title == "Bikroy.com - Electronics, Cars, Property and Jobs in Bangladesh":
            self.logger.info("***** Login with Google Test is Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Login with Google Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Bikroy.com_TestAutomation\\screenshots\\test_003_loginwithGoogle.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Verifying Login with Google Test *****")
        self.logger.info("***** Completed Test_003_loginwithGoogle *****")