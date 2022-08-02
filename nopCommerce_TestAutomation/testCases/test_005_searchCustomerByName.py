import time
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomerPage
from pageObjects.searchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_005_searchCustomerByName:
    baseURL = ReadProperties.getApplicationURL()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("***** Starting Test_005_searchCustomerByName *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Succesful *****")

        self.logger.info("***** Starting Search Customer By Name *****")
        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("***** Searching Customer by Name *****")
        searchcust = SearchCustomerPage(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True == status

        self.logger.info("***** End of Search Customer By Name *****")
        self.logger.info("***** Completed Test_005_searchCustomerByName *****")
