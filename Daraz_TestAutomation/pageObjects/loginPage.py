from selenium.webdriver.common.by import By

class LoginPage:
    textbox_phone_xpath = "//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input"
    textbox_password_xpath = "//*[@id='container']/div/div[2]/form/div/div[1]/div[2]/input"
    button_login_xpath = "//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/button"
    link_login_linktext = "SIGNUP / LOGIN"

    def __init__(self, driver):
        self.driver = driver

    def clickToLoginPage(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linktext).click()

    def setUserPhone(self, userphone):
        self.driver.find_element(By.XPATH, self.textbox_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_phone_xpath).send_keys(userphone)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()