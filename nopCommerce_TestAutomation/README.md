## [@nopCommerce](https://www.nopcommerce.com/en) Test Automation using Page Object Model

## Technology Used:

- Test Tool: Selenium Webdriver
- Language: Python
- Architecture: POM (Page Object Model)
- Framework: Hybrid Framework from Scratch
- IDE: PyCharm

## Pre Requisites:

- selenium: Selenium Libraries
- pytest: Python Unit Test Framework
- pytest-html: Pytest HTML Report
- pytest-xdist: Run Tests Parallel
- openpyxl: MS Excel Support

## The Steps Executed in these Automation are:

## TestCase 01: test_001_homePageTitle
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Get the page title
- Verify the title and take a screenshot if failed
- Close the window

## TestCase 02: test_002_login
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Set username and password and click to login
- Click to 'Login' button
- Verify the login with home page title and take a screenshot if failed
- Close the window

## TestCase 03: test_003_loginDDT
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Set all the usernames and password automatically and try to login through 'Login' button
- Verify the title to confirm login and take a screenshot if failed
- Close the window

## TestCase 04: test_004_addCustomer
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Go to 'Customers' section and eneter into the 'Customers'
- Click to 'Add new' button
- Fiil up all the required fields with valid data and click to 'Save' button
- Verify the add record throug text verification and take a screenshot if failed
- Close the window

## TestCase 05: test_005_searchCustomerbyName
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Go to 'Customers' section and eneter into the 'Customers'
- Fill up the 'First name' and 'Last name' field
- Click to the 'Search' button and observe the result
- Close the window

## TestCase 06: test_006_searchCustomerbyEmail
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Go to 'Customers' section and eneter into the 'Customers'
- Fill up the 'Email' field
- Click to the 'Search' button and observe the result
- Close the window

## TestCase 07: test_007_logout
- Open Chrome browser
- Go to nopCommerce Homepage URL
- Maximize the browser window
- Click to 'Logout'
- Verify the logout with home page title and take a screenshot if failed
- Close the window

## Run the Script:

- Right click on run.bat file
- Run the cases
- Close the program

## Author:

[@Md. Mehedi Hasan](https://github.com/mehedi9021)
