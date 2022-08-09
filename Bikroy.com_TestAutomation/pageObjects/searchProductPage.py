from selenium.webdriver.common.by import By


class SearchProductPage:
    search_box_css = "#app-wrapper > div.top-container--12FJu.all.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-column--3aExp.flex--3fKk1 > div.desktop-max-width-container--3xntY.main-content-area--o-zsx.skeleton-content--2JN5q > div.search-container--1aaDi.justify-content-center--3YVEn.align-items-flex-end--Fg8OY.flex-wrap-nowrap--3IpfJ.flex-direction-row--27fh1.flex--3fKk1 > div > div > form > input"
    search_button_css = "#app-wrapper > div.top-container--12FJu.all.justify-content-flex-start--1Xozy.align-items-normal--vaTgD.flex-wrap-nowrap--3IpfJ.flex-direction-column--3aExp.flex--3fKk1 > div.desktop-max-width-container--3xntY.main-content-area--o-zsx.skeleton-content--2JN5q > div.search-container--1aaDi.justify-content-center--3YVEn.align-items-flex-end--Fg8OY.flex-wrap-nowrap--3IpfJ.flex-direction-row--27fh1.flex--3fKk1 > div > div > form > div > button"
    filter_xpath = "//*[@id='app-wrapper']/div[1]/div[3]/div/div[2]/div[3]/div/div[2]/div[4]/div/label/span[1]"

    def __init__(self, driver):
        self.driver = driver

    def setSearchText(self, text):
        self.driver.find_element(By.CSS_SELECTOR, self.search_box_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.search_box_css).send_keys(text)

    def clicktoSearchButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_css).click()

    def clicktoFilter(self):
        self.driver.find_element(By.XPATH, self.filter_xpath).click()







