import pytest
import time
from selenium import webdriver
from pageObjects.logout import Logout
from selenium.webdriver.common.by import By
from pageObjects.productCategoryPage import ProductCategoryPage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_006_verifyProductCategory:
    baseURL = ReadProperties.getApplicationURL()
    userphone = ReadProperties.getUserPhone()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***** Starting Test_002_login *****")
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

        self.category = ProductCategoryPage(self.driver)
        self.category.hoverCategory()
        time.sleep(3)
        self.category.hoverSubCategory()
        time.sleep(3)
        self.category.clickSubSubCategory()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'Cat Food' in self.msg:
            self.logger.info("***** Item Found *****")
            assert True
        else:
            self.logger.error("***** Item Not Found *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Daraz_TestAutomation\\screenshots\\test_006_verifyProductCategory.png")
            self.driver.close()
            assert False

        # logout
        self.logout = Logout(self.driver)
        self.logout.clickToUserAccount()
        time.sleep(3)
        self.logout.clickToLogout()

        self.driver.close()

        self.logger.info("***** End of Verifying Product Category Test *****")
        self.logger.info("***** Completed Test_006_verifyProductCategory *****")