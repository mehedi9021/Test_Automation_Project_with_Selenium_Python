from selenium.webdriver.common.by import By

class ItemAddtoCartPage:
    item_link_text = "For OnePlus 9 Pro Shockproof Transparent liquid Cristal clear long time useable soft premium protective back cover"
    quantity_button_xpath = "//*[@id='module_quantity-input']/div/div/div/div/div[1]/a[1]/span/i"
    addtocart_button_xpath = "//span[contains(text(),'Add to Cart')]"
    gotocart_button_xpath = "//button[contains(text(),'GO TO CART')]"

    def __init__(self, driver):
        self.driver = driver

    def clickToItem(self):
        self.driver.find_element(By.LINK_TEXT, self.item_link_text).click()

    def clickToAddQuantity(self):
        self.driver.find_element(By.XPATH, self.quantity_button_xpath).click()

    def clickAddToCart(self):
        self.driver.find_element(By.XPATH, self.addtocart_button_xpath).click()

    def clickGoToCart(self):
        self.driver.find_element(By.XPATH, self.gotocart_button_xpath).click()
