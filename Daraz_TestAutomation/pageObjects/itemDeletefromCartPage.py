from selenium.webdriver.common.by import By

class ItemDeletefromCartPage:
    cart_icon_css = "#topActionHeader > div.lzd-header-content > div.lzd-logo-bar > div > div.lzd-nav-cart > a > span.cart-icon > svg"
    itemlist_checkbox_xpath = "//*[@id='listHeader_H']/div/div/div[1]/label/input"
    delete_xpath = "//span[contains(text(),'Delete')]"
    remove_xpath = "//button[contains(text(),'REMOVE')]"

    def __init__(self, driver):
        self.driver = driver

    def clickToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cart_icon_css).click()

    def clickToItemCheckbox(self):
        self.driver.find_element(By.XPATH, self.itemlist_checkbox_xpath).click()

    def clickToDelete(self):
        self.driver.find_element(By.XPATH, self.delete_xpath).click()

    def clickToRemove(self):
        self.driver.find_element(By.XPATH, self.remove_xpath).click()
