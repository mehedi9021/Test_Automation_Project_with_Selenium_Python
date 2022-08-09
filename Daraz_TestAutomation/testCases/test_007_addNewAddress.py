import pytest
import time
from selenium import webdriver
from pageObjects.addNewAddressPage import AddNewAddressPage
from pageObjects.logout import Logout
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_007_addNewAddress:
    baseURL = ReadProperties.getApplicationURL()
    userphone = ReadProperties.getUserPhone()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addNewAddress(self, setup):
        self.logger.info("***** Starting Test_007_addNewAddress *****")
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

        self.useracc = AddNewAddressPage(self.driver)
        self.useracc.clickToUserAccount()
        time.sleep(3)
        self.useracc.clickManageMyAccount()
        self.useracc.clickToAddressBook()
        self.useracc.clickToAddNewAddress()

        self.logger.info("***** Providing New Address *****")
        self.useracc.setFullName("Md. XYZ")
        self.useracc.setPhoneNumber("01111111223")
        self.useracc.setRegion()
        self.useracc.setCity()
        self.useracc.setArea()
        self.useracc.setAddress("Haziganj")
        time.sleep(3)
        self.useracc.clickToHomeIcon()
        time.sleep(5)
        self.useracc.clickToSave()
        time.sleep(5)
        self.logger.info("***** Address Added Successfully *****")

        # logout
        self.logout = Logout(self.driver)
        self.logout.clickToUserAccount()
        time.sleep(3)
        self.logout.clickToLogout()

        self.driver.close()

        self.logger.info("***** End of Add New Address Test *****")
        self.logger.info("***** Completed Test_007_addNewAddress *****")