from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    login_icon_xpath = "#app-wrapper > div.top-container--12FJu.all.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-column--3aExp.flex--3fKk1 > div:nth-child(2) > div > nav > div > ul:nth-child(2) > li.login-icon-container--3oQMU > div > a > span"
    continue_with_email_button_xpath = "//span[contains(text(),'Continue with Email')]"
    continue_with_google_button_xpath = "//span[contains(text(),'Continue with Google')]"
    textbox_email_xpath = "//input[@id='input_email']"
    textbox_password_xpath = "//input[@id='input_password']"
    test_email_box_name = "identifier"
    test_password_box_name = "password"
    button_email_next_css = "#identifierNext > div > button > span"
    button_password_next_css = "#passwordNext > div > button > span"
    button_login_xpath = "//button[contains(text(),'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def clickToLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_icon_xpath).click()

    def clickContinuewithEmail(self):
        self.driver.find_element(By.XPATH, self.continue_with_email_button_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickContinuewitGoogle(self):
        self.driver.find_element(By.XPATH, self.continue_with_google_button_xpath).click()

    def setTestEmail(self, temail):
        self.driver.find_element(By.NAME, self.test_email_box_name).send_keys(temail)

    def setTestPassword(self, tpassword):
        self.driver.find_element(By.NAME, self.test_password_box_name).send_keys(tpassword)

    def clicktoEmailNext(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_email_next_css).click()

    def clicktoPasswordNext(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_password_next_css).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()