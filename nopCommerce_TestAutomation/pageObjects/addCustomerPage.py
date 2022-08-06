import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomerPage:
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstitemYourStoreName_xpath = "//*[@id='c8208a21-6bde-4648-8b48-24f26ce246f1']"
    lstitemTestScore2_xpath = "//li[contains(text(),'Test store 2')]"
    txtCustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpManagerofvendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        time.sleep(3)
        if newsletter == 'Your store name':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStoreName_xpath)
        elif newsletter == 'Test store 2':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemTestScore2_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemTestScore2_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]").click()
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpManagerofvendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()