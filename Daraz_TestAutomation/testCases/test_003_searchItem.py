import pytest
import time
from selenium import webdriver
from pageObjects.logout import Logout
from selenium.webdriver.common.by import By
from pageObjects.searchItemPage import SearchItemPage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_003_searchItem:
    baseURL = ReadProperties.getApplicationURL()
    userphone = ReadProperties.getUserPhone()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***** Starting Test_003_searchItem *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.clickToLoginPage()
        self.lp.setUserPhone(self.userphone)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Verifying Search Item Test *****")
        self.searchitem = SearchItemPage(self.driver)
        self.searchitem.setSearchText("oneplus 9 back cover")
        self.searchitem.clickSearchButton()

        self.logger.info("***** Search Item Validation Started *****")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'Search No Result' in self.msg:
            self.logger.error("***** Item Not Found *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Daraz_TestAutomation\\screenshots\\test_003_searchItem.png")
            self.driver.close()
            assert False
        else:
            self.logger.info("***** Item Found *****")
            assert True

        # logout
        self.logout = Logout(self.driver)
        self.logout.clickToUserAccount()
        time.sleep(3)
        self.logout.clickToLogout()

        self.driver.close()

        self.logger.info("***** End of Search Item Test *****")
        self.logger.info("***** Completed Test_003_searchItem *****")

