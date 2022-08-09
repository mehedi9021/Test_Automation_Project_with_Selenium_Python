import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.searchProductPage import SearchProductPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_005_searchProduct:
    baseURL = ReadProperties.getApplicationURL()
    logger = CustomLogger.loggen()

    @pytest.mark.regression
    def test_searchProduct(self, setup):
        self.logger.info("***** Starting Test_005_searchProduct *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.sp = SearchProductPage(self.driver)
        self.sp.setSearchText("oneplus mobile")
        self.sp.clicktoSearchButton()
        time.sleep(3)
        self.sp.clicktoFilter()
        time.sleep(5)

        text = self.driver.find_element(By.CSS_SELECTOR, "body.bgwhite:nth-child(2) div.container--297Nx.all div.main-section--3D6zE div.row--3Vhjr.main-container--28aG5.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-wrap--2PCx8.flex-direction-row--27fh1.flex--3fKk1:nth-child(2) div.sm-col-12--30zDS.lg-col-9--20qCf.block--3v-Ow:nth-child(4) div.ad-list-container--1UnyA div:nth-child(1) div.ad-list--2Y3ql div.list-wrapper--t_A02:nth-child(1) ul.list--3NxGO > li.normal--2QYVk.gtm-normal-ad:nth-child(1)").text
        print(text)

        if "OnePlus" in text:
            self.logger.info("***** Product Found *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Product Not Found *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Bikroy.com_TestAutomation\\screenshots\\test_005_searchProduct.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Search Product Test *****")
        self.logger.info("***** Completed Test_005_searchProduct *****")