import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.logout import Logout
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger
from utilities import XLUtils
import time

class Test_003_loginDDT():
    baseURL = ReadProperties.getApplicationURL()
    path = "C:\\Users\\User\\PycharmProjects\\nopCommerce_TestAutomation\\testData\\loginData.xlsx"
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_loginDDT(self, setup):
        self.logger.info("***** Starting Test_003_loginDDT *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("***** Starting Login DDT Test *****")
        self.lp = LoginPage(self.driver)
        self.logout = Logout(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows:', self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***** Passed *****")
                    self.logout.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("***** Failed *****")
                    self.logout.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***** Failed *****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("***** Passed *****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** DDT Login Test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** DDT Login Test Failed *****")
            self.driver.close()
            assert False

        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("***** Completed  Test_003_loginDDT *****")