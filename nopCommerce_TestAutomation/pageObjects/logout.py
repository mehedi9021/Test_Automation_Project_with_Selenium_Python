from selenium.webdriver.common.by import By

class Logout:
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()