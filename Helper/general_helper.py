from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helper.json_parser import parse_json
import logging
import time

import random 

class GeneralHelper():
    def __init__(self, driver):
        self.driver = driver
        self.my_config = 'my_config.json'

    def navigate_to_url(self):
        try:
            config = parse_json(self.my_config)
            url = config["url"]
            if url:
                self.driver.get(url)
                self.driver.set_page_load_timeout(20)
                logging.info(f"Navigated to URL: '{url}'")
                return self.driver
            else:
                logging.warning("URL not found in configuration.")
        except Exception as e:
            logging.error(f"Failed to navigate to URL. Error: {str(e)}")

    def open_new_tab(self, driver, url):
        try:
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            logging.info(f"Opened a new tab with URL: {url}")
        except Exception as e:
            logging.error(f"Error opening a new tab: {e}")
            raise
            
    def find_elem_in_ui(self, locator, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)  
                )                                                                             
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logging.info(f"Element {locator} found and is now visible.")
            return element
        
        except Exception as e:
            logging.error(f"Error finding element {locator} or waiting for visibility: {e}")
        
    def find_elem_in_dom(self, locator, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator) 
            )
            logging.info(f"Element {locator} found and is now present.")
            return element
        except Exception as e:
            logging.error(f"Error finding element {locator} or waiting for presence: {e}")
            raise

    def find_and_click_elem(self, locator, timeout=120):
        try:
            element = self.driver.find_element(*locator)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)
            )
            element.click()
            logging.info(f"Clicked on element {locator}.")
            return element
    
        except Exception as e:
            logging.error(f"Error finding element {locator} or clicking: {e}")
            raise
        
    def find_elem_and_send_data(self, locator, input_data, timeout=120):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.send_keys(input_data)
            logging.info(f"Sent keys '{input_data}' to element {locator}.")
            return element
    
        except Exception as e:
            logging.error(f"Error finding element {locator} or sending keys: {e}")
            raise
        
    def find_elements_in_ui(self, locator, timeout=360):
        try:
            # time.sleep(1)
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator) 
            )
            for element in elements:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            logging.info(f"Element {locator} found and is now present. Scrolled to each element.")
            return elements
        except Exception as e:
            logging.error(f"Error finding element {locator} or waiting for presence: {e}")
            raise
        
    def extract_elem_text(self, locator):
        try:
            elem = self.find_elem_in_ui(locator)
            elem_text = elem.text
            logging.info(f"Title: '{elem_text}'. Extraction complete.")
            return elem_text
        except Exception as e:
            logging.error(f"An error occurred during text extraction: {str(e)}")    
        
    
    
# add screenshot method also in pages 
#also change my_config path 
        
    