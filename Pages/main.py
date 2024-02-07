from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Helper.general_helper import GeneralHelper
import logging
import time

class MainPage(GeneralHelper):
    ul_page_titles = (By.XPATH, "//ul[@class='products__list']//h3[text()]")
    inp_search = (By.XPATH, "//div//input[@type='search']")
    ul_pagination = (By.XPATH, "//ul[@class='pagination__pages']//li//a")
    link_next_page = (By.XPATH,"//a[@aria-label='Next page']")
    link_sign_in =  (By.XPATH,"//ul//li//a[contains(text(), 'Sign')]")
    img_logo = (By.XPATH, "//section[contains(@class, 'header__logo')]")
    
    def click_sign_in(self):
        try:
            self.find_and_click_elem(self.link_sign_in)
            logging.info('Navigating to Sign-In page.')
        except Exception as e:
            logging.error(f'Failed to click Sign-In link: {str(e)}')
    
    def click_logo(self):
        try:
            self.find_and_click_elem(self.img_logo)
            self.driver.set_page_load_timeout(20)
            logging.info("Logo clicked successfully.")
        except Exception as e:
                logging.error(f"An error occurred while clicking the logo: {str(e)}")
                   
    def search_data(self, input_data):
        try:
            logging.info(f"Searching for data: {input_data}")
            el_search = self.find_elem_and_send_data(self.inp_search, input_data)
            el_search.send_keys(Keys.ENTER)
            self.driver.set_page_load_timeout(20)
            logging.info("Search successful.")
        except Exception as e:
            logging.error(f"An error occurred during search for data '{input_data}': {str(e)}")
  
    def extract_elements_text(self):
        try:
            logging.info("Extracting page data...")
            page_output = []
            page_titles = self.find_elements_in_ui(self.ul_page_titles)
            for title in page_titles:
                title_text = title.text
                page_output.append(title_text)
                logging.info(f"Title: {title_text}")
            logging.info("Extraction complete.")
            return page_output
        except Exception as e:
            logging.error(f"An error occurred during page data extraction: {str(e)}")
    
    def extract_titles(self, input_data):
        try:
            self.click_logo()
            self.search_data(input_data)
            all_pages = self.find_elements_in_ui(self.ul_pagination)
            num_of_pages = int(all_pages[-2].text)
            final_out = []
            for num in range(num_of_pages):
                try:
                    page_output = self.extract_elements_text()
                    final_out.append({
                        num: page_output
                    })
                except Exception as e:
                    logging.error(f"Error during page extraction on page {num + 1}: {str(e)}")
                    
                self.find_and_click_elem(self.link_next_page) 
                time.sleep(1)
                self.driver.set_page_load_timeout(20)
                logging.info("Page title checking complete.")
            
        except Exception as e:
                logging.error(f"An error occurred during page title checking: {str(e)}")
    
       
            

            
            
        
            
        
        
        
         
 
        
        
    
    
    
    
    
    





    
    