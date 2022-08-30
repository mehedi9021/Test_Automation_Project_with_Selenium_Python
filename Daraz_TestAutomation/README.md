## @Daraz Test Automation using Page Object Model

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

## The Steps executed in these Automation are:

## TestCase 01: test_001_homePageTitle
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Get the page title
- Verify the title and take a screenshot if failed
- Close the window

## TestCase 02: test_002_login
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Click to SIGNUP / LOGIN
- Provide user phone no. and password
- Click to login button
- Verify the login with home page title and take a screenshot if failed
- Click to logout

## TestCase 03: test_003_searchItem
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Perform login
- Enter a product name in search box
- Click to search icon
- Verify the search result and take a screenshot if failed
- Click to logout

## TestCase 04: test_004_itemAddtoCart
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Perform login
- Search a product
- Click to the item from search result
- Click to add quantity
- Click add to cart button
- Verify the product added successfully and take a screenshot if failed
- Click to logout

## TestCase 05: test_005_itemDeletefromCart
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Perform login
- Click to cart icon
- Select all the items
- Click to delete button
- Verify the products are deleted and take a screenshot if failed
- Click to logout

## TestCase 06: test_006_verifyProductCategory
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Perform login
- Hover over the category
- Hover over the sub-category
- Click to 'Cat Food'
- Verify the result and take a screenshot if failed
- Click to logout

## TestCase 06: test_007_addNewAddress
- Open Chrome browser
- Go to Daraz Homepage URL
- Maximize the browser window
- Perform login
- Click to user's account
- Click to 'Manage My Account'
- Click to 'Address Book'
- Click to 'Add New Address'
- Fill up all the fileds
- Click to 'Save' Button
- Click to logout

## Run the Script:

- Right click on run.bat file
- Run the cases
- Close the program

## Author:

- [@Md. Mehedi Hasan](https://github.com/mehedi9021)
