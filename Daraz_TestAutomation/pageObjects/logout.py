from selenium.webdriver.common.by import By

class Logout:
    link_text_user_account_id = "myAccountTrigger"
    link_text_logout = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clickToUserAccount(self):
        self.driver.find_element(By.ID, self.link_text_user_account_id).click()

    def clickToLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_text_logout).click()
