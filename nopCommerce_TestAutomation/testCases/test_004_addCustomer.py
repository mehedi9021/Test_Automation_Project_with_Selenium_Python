import pytest
import time
import string
import random
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomerPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger
from selenium.webdriver.common.by import By


class Test_004_addCustomer:
    baseURL = ReadProperties.getApplicationURL()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("***** Starting Test_004_addCustomer *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Succesful *****")

        self.logger.info("***** Starting Add Customer Test *****")
        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("***** Providing Customer Info *****")
        self.addcust.setEmail("nopcommercemail11@gmail.com")
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Md. Mehedi")
        self.addcust.setLastName("Hasan")
        self.addcust.setGender("Male")
        self.addcust.setDob("11/09/1997")  # Format: D / MM / YYY
        self.addcust.setCompanyName("SQA Zone")
        self.addcust.setNewsletter("Test store 2")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing.....")
        self.addcust.clickOnSave()
        self.logger.info("***** Saving Customer Info *****")

        self.logger.info("***** Add Customer Validation Started *****")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            self.logger.info("***** Add Customer Test Passed *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\nopCommerce_TestAutomation\\screenshots\\test_004_addCustomer.png")
            self.logger.error("***** Add customer Test Failed *****")
            self.driver.close()
            assert False

        self.logger.info("***** End of Add Customer Test *****")
        self.logger.info("***** Completed Test_004_addCustomer *****")