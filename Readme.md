This project is a test automation framework for: https://courses.ultimateqa.com/collections  

Framework have 2 test cases: 
1. Search for an existing course, check that the titles of the found courses contain the searched data
2. Search for a non-existing course, check that the “no results were found” message is visible

## Helper
### general_helper
The file includes various utility functions commonly used across the project.
### json_parser
The file contains functions to parse and manipulate JSON data, including reading from and writing to JSON files.

## Pages
### Login Page
The Login Page contains functions for user authentication.
#### `click_create_account()`
This function navigates to the account creation page.
#### `login_to_account()`
This function is responsible for logging into the account. It retrieves user credentials from the my_config.json file and performs the necessary actions to log in.

### Main Page
The Main Page represents the main interface of the application.
#### `click_sign_in()` 
Initiates the click action on the "Sign In" button, typically navigating to the login page.
#### `click_logo()`
Performs a click action on the application logo, commonly used to return to the main page.
#### `search_data()`
Executes a search action.
#### `get_titles()`
Returns a collection of titles of each page, which can be used for further verification.
#### `check_titles_for_keyword()`
Check a collection of titles for the presence of a specified keyword, generating a list of issues for any titles that don't contain the keyword.

### Register Page
The Register Page handles user registration and dynamically updates the `my_config.json` file with new user credentials.
#### `register_account()`
This function function registers an account using the generated credentials from the `test_data.py` file. It fills the registration form with the test data and send it.

## Test Data
### test_data
The file contains register credentials generated using Faker.

## Tests
### test_1_check_titles
This test registers with a valid user, logs in with the created credentials, and searches for 'selenium' courses. It checks that the titles of the found courses contain the searched data.
### test_2_check_no_result
This test logs in with valid credentials and searches for a non-existing course. It verifies that the “no results were found” message is visible.

## Configuration Files
### my_config.json
This JSON file includes the URL, email, and password - which are updated during user registration.
### conftest.json
 This file serves as a shared configuration file in pytest project, providing a driver fixture for Selenium WebDriver setup (configured for Chrome) and setting up logging for test modules.

## Requirements
The file lists the Python libraries and their versions that must be installed to satisfy the dependencies of the project.


