import pytest
import time
from selenium import webdriver
from pageObjects.itemAddToCartPage import ItemAddToCartPage
from pageObjects.logout import Logout
from selenium.webdriver.common.by import By
from pageObjects.searchItemPage import SearchItemPage
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_004_itemAddToCartPage:
    baseURL = ReadProperties.getApplicationURL()
    userphone = ReadProperties.getUserPhone()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
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

        self.searchitem = SearchItemPage(self.driver)
        self.searchitem.setSearchText("oneplus 9 back cover")
        self.searchitem.clickSearchButton()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'Search No Result' in self.msg:
            self.logger.error("***** Item Not Found *****")
            self.driver.close()
            assert False
        else:
            self.logger.info("***** Item Found *****")
            assert True
            # item add to cart
            self.addtocart = ItemAddToCartPage(self.driver)
            self.addtocart.clickToItem()
            self.addtocart.clickToAddQuantity()
            self.addtocart.clickAddToCart()
            time.sleep(3)
            self.addtocart.clickGoToCart()

            self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            print(self.msg)

            if 'For OnePlus 9 Pro Shockproof Transparent liquid Cristal clear long time useable soft premium protective back cover' in self.msg:
                self.logger.info("***** Added to Cart Successfully *****")
                assert True
            else:
                self.logger.error("***** Item Not Found *****")
                self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Daraz_TestAutomation\\screenshots\\test_004_itemAddToCartPage.png")
                self.driver.close()
                assert False

        # logout
        self.logout = Logout(self.driver)
        self.logout.clickToUserAccount()
        time.sleep(3)
        self.logout.clickToLogout()

        self.driver.close()

        self.logger.info("***** End of Item Add to Cart Test *****")
        self.logger.info("***** Completed Test_004_itemAddToCartPage *****")

