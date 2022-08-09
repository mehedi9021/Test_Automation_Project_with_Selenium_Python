from selenium.webdriver.common.by import By

class SearchItemPage:
    search_box_xpath = "//input[@id='q']"
    searc_button_xpath = "//button[contains(text(),'SEARCH')]"

    def __init__(self, driver):
        self.driver = driver

    def setSearchText(self, searchtext):
        self.driver.find_element(By.XPATH, self.search_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(searchtext)

    def clickSearchButton(self):
        self.driver.find_element(By.XPATH, self.searc_button_xpath).click()