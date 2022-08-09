import time

import pytest
from selenium import webdriver
from pageObjects.adPostPage import AddPostPage
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadProperties
from utilities.customLogger import CustomLogger

class Test_006_adPost:
    baseURL = ReadProperties.getApplicationURL()
    email = ReadProperties.getEmail()
    password = ReadProperties.getPassword()
    logger = CustomLogger.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_adPost(self, setup):
        self.logger.info("***** Starting Test_006_adPost *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.ap = AddPostPage(self.driver)
        self.ap.clicktoPostYourAd()

        self.log = LoginPage(self.driver)
        self.driver.implicitly_wait(50)
        self.log.clickContinuewithEmail()
        self.log.setEmail(self.email)
        self.log.setPassword(self.password)
        self.log.clickLogin()
        self.logger.info("***** Login Successfully *****")

        self.driver.implicitly_wait(50)
        self.ap.selectSellSomething()
        self.driver.implicitly_wait(50)
        self.ap.selectCategory()
        self.driver.implicitly_wait(50)
        time.sleep(5)
        self.ap.selectSubCategory()
        self.driver.implicitly_wait(50)

        self.logger.info("***** Filling up Details *****")
        self.ap.selectCondition()
        self.ap.selectAuthenticity()
        time.sleep(3)
        self.ap.selectBrand()
        time.sleep(5)
        self.ap.selectModel()
        time.sleep(5)
        self.ap.setEdition("China")
        self.driver.implicitly_wait(50)
        self.ap.selectFeatures()
        self.driver.implicitly_wait(50)
        self.ap.setDescription("Almost new condition. If anyone interested please knock.")
        self.driver.implicitly_wait(50)
        self.ap.setPrice("500")
        self.driver.implicitly_wait(50)
        self.ap.selectNegotiable()
        self.driver.implicitly_wait(50)
        time.sleep(5)
        self.ap.addPhotos("C:\\Users\\User\\PycharmProjects\\Bikroy.com_TestAutomation\\images\Capture.PNG")
        self.driver.implicitly_wait(50)
        self.ap.selectTermsandConditions()
        self.driver.implicitly_wait(50)
        self.ap.clickToPostAd()

        text = self.driver.find_element(By.CSS_SELECTOR, "#app-wrapper > div.top-container--12FJu.all.skeleton-container--1ZnjY.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-column--3aExp.flex--3fKk1 > div.desktop-max-width-container--3xntY.main-content-area--o-zsx.skeleton-content-promotions--3nFep > div.row--3Vhjr.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-wrap--2PCx8.flex-direction-row--27fh1.flex--3fKk1 > div.sm-col-12--30zDS.lg-col-5--2354Y.payment-info--29SKS.block--3v-Ow > div.container--3gb4O").text
        print(text)

        if "Your ad is under review!" in text:
            self.logger.info("***** Posted Successfully *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Failed to Post *****")
            self.driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\Bikroy.com_TestAutomation\\screenshots\\test_006_adPost.png")
            self.driver.close()
            assert False

        self.logger.info("***** End of Ad Post Test *****")
        self.logger.info("***** Completed Test_006_adPost *****")