from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path = "C:\Driver\chromedriver.exe")
    return driver

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Daraz_TestAutomation'
    config._metadata['Module Name'] = 'Daraz Web App Testing'
    config._metadata['Tester'] = 'Md. Mehedi Hasan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Python_Home", None)
    metadata.pop("Plugins", None)