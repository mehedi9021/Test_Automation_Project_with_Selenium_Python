import pytest
import time
from selenium import webdriver
from pageObjects.logout import Logout
from pageObjects.itemDeletefromCartPage import ItemDeletefromCartPage
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_005_itemDeletefromCart:
    baseURL = ReadProperties.getApplicationURL()
    userphone = ReadProperties.getUserPhone()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_itemDeletefromCart(self, setup):
        self.logger.info("***** Starting Test_005_itemDeletefromCart *****")
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

        self.itemdelete = ItemDeletefromCartPage(self.driver)
        self.itemdelete.clickToCart()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'There are no items in this cart' in self.msg:
            self.logger.error("***** No Item to Delete *****")
            self.driver.close()
            assert False
        else:
            self.itemdelete.clickToItemCheckbox()
            self.itemdelete.clickToDelete()
            time.sleep(3)
            self.itemdelete.clickToRemove()
            time.sleep(3)
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            print(self.msg)
            if 'There are no items in this cart' in self.msg:
                self.logger.info("***** Successfully Deleted *****")
                assert True
            else:
                self.logger.error("***** Not Deleted *****")
                self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Daraz_TestAutomation\\screenshots\\test_005_itemDeletefromCart.png")
                self.driver.close()
                assert False
            assert True

        # logout
        self.logout = Logout(self.driver)
        self.logout.clickToUserAccount()
        time.sleep(3)
        self.logout.clickToLogout()

        self.driver.close()

        self.logger.info("***** End of Item Delete From Cart Test *****")
        self.logger.info("***** Completed Test_005_itemDeletefromCart *****")