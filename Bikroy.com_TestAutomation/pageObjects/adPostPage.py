import time

from selenium.webdriver.common.by import By


class AddPostPage:
    post_your_ad_css = "#app-wrapper > div.top-container--12FJu.all.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-column--3aExp.flex--3fKk1 > div:nth-child(2) > div > nav > div > ul:nth-child(2) > li:nth-child(3) > a > button"
    sell_something_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[2]/div[2]/div[1]/ul/li[1]/button"
    select_category_xpath = "/html/body/div[6]/div/div/div/div[2]/div/div/div/ul/li[1]/button/div"
    select_subcategory_xpath = "/html/body/div[6]/div/div/div/div[2]/div/div[2]/div/ul/li[1]/button/div/div"
    condition_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[1]/div/div[2]/div/div[1]/label/span"

    authenticity_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[2]/div/div[2]/div/div[1]/label/span"
    select_brand_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[3]/div/div[1]/div[1]/div[1]/button/span"
    brand_xpath = "//*[@id='downshift-0-item-67']"
    select_model_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[3]/div/div[1]/div[2]/div[1]/button/span"
    model_xpath = "//*[@id='downshift-1-item-52']"
    edition_textbox_xpath = "//*[@id='input_edition']"
    feature_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[5]/div/div[2]/div/div[1]/label/span"
    description_textbox_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[6]/div/div[1]/textarea"
    price_textbox_xpath = "//*[@id='input_price']"
    select_negotiable_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[1]/div[7]/div[2]/div/div/label/span"
    upload_image1_css = "#app-wrapper > div.top-container--12FJu.all.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-column--3aExp.flex--3fKk1 > div.desktop-max-width-container--3xntY.main-content-area--o-zsx > div:nth-child(5) > form > div:nth-child(3) > div > div.grid-container--16MBA > ul > li:nth-child(1) > div > label > div > div > div"
    term_condition_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[5]/div[2]/label/span"
    post_ad_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div[5]/form/div[5]/div[3]/button"

    def __init__(self, driver):
        self.driver = driver

    def clicktoPostYourAd(self):
        self.driver.find_element(By.CSS_SELECTOR, self.post_your_ad_css).click()

    def selectSellSomething(self):
        self.driver.find_element(By.XPATH, self.sell_something_xpath).click()

    def selectCategory(self):
        self.driver.find_element(By.XPATH, self.select_category_xpath).click()

    def selectSubCategory(self):
        self.driver.find_element(By.XPATH, self.select_subcategory_xpath).click()

    def selectCondition(self):
        self.driver.find_element(By.XPATH, self.condition_xpath).click()

    def selectAuthenticity(self):
        self.driver.find_element(By.XPATH, self.authenticity_xpath).click()

    def selectBrand(self):
        self.driver.find_element(By.XPATH, self.select_brand_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.brand_xpath).click()

    def selectModel(self):
        self.driver.find_element(By.XPATH, self.select_model_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.model_xpath).click()

    def setEdition(self, edition):
        self.driver.find_element(By.XPATH, self.edition_textbox_xpath).send_keys(edition)

    def selectFeatures(self):
        self.driver.find_element(By.XPATH, self.feature_xpath).click()

    def setDescription(self, description):
        self.driver.find_element(By.XPATH, self.description_textbox_xpath).send_keys(description)

    def setPrice(self, price):
        self.driver.find_element(By.XPATH, self.price_textbox_xpath).send_keys(price)

    def selectNegotiable(self):
        self.driver.find_element(By.XPATH, self.select_negotiable_xpath).click()

    def addPhotos(self, photos):
        self.driver.find_element(By.XPATH, self.upload_image1_css).send_keys(photos)

    def selectTermsandConditions(self):
        self.driver.find_element(By.XPATH, self.term_condition_xpath).click()

    def clickToPostAd(self):
        self.driver.find_element(By.XPATH, self.post_ad_xpath).click()