## [@Bikroy.com](https://bikroy.com/) Test Automation using Page Object Model

## Technology Used

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
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Get the page title
- Verify the title and take a screenshot if failed
- Close the window

## TestCase 02: test_002_loginwithEmail
- Open Chrome browser
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Click to login icon
- Click to 'Continue with Email' button
- Set email and password then click to login button
- Verify the login with home page title and take a screenshot if failed
- Close the window

## TestCase 03: test_003_loginwithGoogle
- Open Chrome browser
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Click to login icon
- Click to 'Continue with Google' button
- Set email and password then click to login
- Verify the login with home page title and take a screenshot if failed
- Close the window

## TestCase 04: test_004_selectLocation
- Open Chrome browser
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Click to location button
- Click to select city
- Click to select area
- Verify the location throug text verification and take a screenshot if failed
- Close the window

## TestCase 05: test_005_searchProduct
- Open Chrome browser
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Enter a product name in search box
- Click to search icon
- Verify the searching result throug text verification and take a screenshot if failed
- Close the window 

## TestCase 06: test_006_adPost
- Open Chrome browser
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Click to 'POST YOUR AD' button
- Click to 'Sell an item, property or service' from 'Sell Something' box
- Click to select a category and then sub-category
- Fill up all the necessary fields
- Click to 'Post ad' button
- Close the window 

## TestCase 07: test_007_logout
- Open Chrome browser
- Go to Bikroy.com Homepage URL
- Maximize the browser window
- Perform login
- Click to 'My account'
- Click to 'Settings'
- Click to 'Logout' button
- Close the window

## Run the Script:

- Right click on run.bat file
- Run the cases
- Close the program

## Author

- [@Md. Mehedi Hasan](https://github.com/mehedi9021)
