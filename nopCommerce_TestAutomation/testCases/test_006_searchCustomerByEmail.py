import time
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomerPage import AddCustomerPage
from pageObjects.searchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_006_searchCustomerByEmail:
    baseURL = ReadProperties.getApplicationURL()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("***** Starting Test_006_searchCustomerByEmail *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Succesful *****")

        self.logger.info("***** Starting Search Customer By Email *****")
        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("***** Searching Customer by Email *****")
        searchcust = SearchCustomerPage(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status

        self.logger.info("***** End of Search Customer By Email *****")
        self.logger.info("***** Completed Test_006_searchCustomerByEmail *****")