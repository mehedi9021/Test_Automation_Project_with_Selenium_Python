from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AddNewAddressPage:
    user_account_id = "myAccountTrigger"
    link_text_manage_account = "Manage My Account"

    addressbook_xpath = "//a[contains(text(),'Address Book')]"
    addnewaddress_button_xpath = "//button[contains(text(),'+ ADD NEW ADDRESS')]"

    fullname_textbox_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[1]/div[1]/input"
    phoneno_textbox_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[1]/div[2]/input"
    region_select_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[2]/div[1]/span/span"
    region_name = "Chattogram"
    city_select_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[2]/div[2]/span/span"
    city_name = "Chandpur Sadar"
    area_select_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[2]/div[3]/span/span"
    area_name = "Chandpur Sadar Baburhat"
    address_textbox_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[2]/div[4]/input"
    select_home_icon_xpath = "//*[@id='container']/div/div/form/div/div[1]/div[2]/div[5]/div/div[2]"
    save_button_css_selector = "#container > div > div > form > div > div.mod-address-form-action > button.next-btn.next-btn-primary.next-btn-large.mod-address-form-btn"

    def __init__(self, driver):
        self.driver = driver

    def clickToUserAccount(self):
        self.driver.find_element(By.ID, self.user_account_id).click()

    def clickManageMyAccount(self):
        self.driver.find_element(By.LINK_TEXT, self.link_text_manage_account).click()

    def clickToAddressBook(self):
        self.driver.find_element(By.XPATH, self.addressbook_xpath).click()

    def clickToAddNewAddress(self):
        self.driver.find_element(By.XPATH, self.addnewaddress_button_xpath).click()

    def setFullName(self, fullname):
        self.driver.find_element(By.XPATH, self.fullname_textbox_xpath).send_keys(fullname)

    def setPhoneNumber(self, phone):
        self.driver.find_element(By.XPATH, self.phoneno_textbox_xpath).send_keys(phone)

    def setRegion(self):
        self.driver.find_element(By.XPATH, self.region_select_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.region_name).click()

    def setCity(self):
        self.driver.find_element(By.XPATH, self.city_select_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.city_name).click()

    def setArea(self):
        self.driver.find_element(By.XPATH, self.area_select_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.area_name).click()

    def setAddress(self, address):
        self.driver.find_element(By.XPATH, self.address_textbox_xpath).send_keys(address)

    def clickToHomeIcon(self):
        self.driver.find_element(By.XPATH, self.select_home_icon_xpath).click()

    def clickToSave(self):
        self.driver.find_element(By.CSS_SELECTOR, self.save_button_css_selector).click()









