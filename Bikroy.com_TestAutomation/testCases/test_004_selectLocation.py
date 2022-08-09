import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.selectLocationPage import SelectLocationPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_004_selectLocation:
    baseURL = ReadProperties.getApplicationURL()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_selectLocation(self, setup):
        self.logger.info("***** Starting Test_004_selectLocation *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.sl = SelectLocationPage(self.driver)
        self.sl.clicktoLocationButton()
        self.driver.implicitly_wait(50)
        self.sl.selectCities()
        self.driver.implicitly_wait(50)
        self.sl.selectAreas()
        self.driver.implicitly_wait(50)
        text = self.driver.find_element(By.XPATH, "//*[@id='app-wrapper']/div[2]/div[3]/div[2]/div/button/span").text
        print(text)

        if text == "Dhaka":
            self.logger.info("***** Select Location Test is Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Select Location Test is Failed *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Bikroy.com_TestAutomation\\screenshots\\test_004_selectLocation.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Select Location Test *****")
        self.logger.info("***** Completed Test_004_selectLocation *****")