from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Logout:
    settings_xpath = "/html/body/div[2]/div/div/div/div/div[1]/nav/ul/li[4]/a"
    logout_button_xpath = "//*[@id='my-content']/div[2]/div[2]/div/a"
    my_account_xpath = "/html/body/nav/div/ul[3]/li[3]/a/span"

    def __init__(self, driver):
        self.driver = driver

    def clicktoMyAccount(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def clicktoSettings(self):
        self.driver.find_element(By.XPATH, self.settings_xpath).click()

    def clicktoLogoutButton(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

