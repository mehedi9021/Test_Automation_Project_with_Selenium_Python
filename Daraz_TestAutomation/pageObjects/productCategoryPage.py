from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductCategoryPage:
    category_xpath = "//span[contains(text(),'Groceries & Pets')]"
    sub_category_xpath = "//*[@id='J_3442298940']/div/ul/ul[5]/li[6]/a/span"
    sub_sub_category_link_text = "Cat Food"

    def __init__(self, driver):
        self.driver = driver

    def hoverCategory(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.driver.find_element(By.XPATH, self.category_xpath))
        self.actions.perform()


    def hoverSubCategory(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.driver.find_element(By.XPATH, self.sub_category_xpath))
        self.actions.perform()

    def clickSubSubCategory(self):
        self.driver.find_element(By.LINK_TEXT, self.sub_sub_category_link_text).click()

