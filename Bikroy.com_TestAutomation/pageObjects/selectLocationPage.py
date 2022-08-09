from selenium.webdriver.common.by import By

class SelectLocationPage:
    location_button_xpath = "//span[contains(text(),'All of Bangladesh')]"
    cities_xpath = "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/ul/li[1]/button/div/div[1]"
    areas_xpath = "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/ul/li[1]/button/div/div"
    location_verify_text_area_xpath = "//body/div[@id='app-container']/div[@id='app-wrapper']/div[1]/div[3]/div[2]/div[1]"


    def __init__(self, driver):
        self.driver = driver

    def clicktoLocationButton(self):
        self.driver.find_element(By.XPATH, self.location_button_xpath).click()

    def selectCities(self):
        self.driver.find_element(By.XPATH, self.cities_xpath).click()

    def selectAreas(self):
        self.driver.find_element(By.XPATH, self.areas_xpath).click()