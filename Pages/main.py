from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Helper.general_helper import GeneralHelper
import logging
import time

class MainPage(GeneralHelper):
    ul_page_titles = (By.XPATH, "//ul[@class='products__list']//h3[text()]")
    ul_pagination = (By.XPATH, "//ul[@class='pagination__pages']//li//a")
    inp_search = (By.XPATH, "//div//input[@type='search']")
    link_next_page = (By.XPATH,"//a[@aria-label='Next page']//i")
    link_sign_in =  (By.XPATH,"//ul//li//a[contains(text(), 'Sign')]")
    img_logo = (By.XPATH, "//section[contains(@class, 'header__logo')]")
    loc_no_result = (By.XPATH, "//div//p[contains(text(), 'results')]")

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
        except Exception as e:
            logging.error(f"An error occurred during search for data '{input_data}': {str(e)}")

    def get_titles(self, input_data):
        try:
            self.click_logo()
            self.search_data(input_data)
            #get pages count
            all_pages = self.find_elements_in_ui(self.ul_pagination)
            num_of_pages = int(all_pages[-2].text)
            final_out = []

            for num in range(1, num_of_pages + 1):
                try:
                    page_output = self.extract_elements_text(self.ul_page_titles)
                    final_out.append({
                        num: page_output
                    })
                except Exception as e:
                    logging.error(f"Error during page extraction on page {num + 1}: {str(e)}")

                try:
                    time.sleep(1) #without can't find locator:(
                    if num == num_of_pages:
                        break
                    else:
                        self.find_and_click_elem(self.link_next_page)
                        logging.info("Page title checking complete.")

                except Exception as e:
                    logging.error(f"Error while navigating to the next page: {str(e)}")
            return final_out    
        
        except Exception as e:
            logging.error(f"An error occurred during page title checking: {str(e)}")
            
    def check_titles_for_keyword(self, final_out, keyword):
        try:
            issues = []

            for page_dict in final_out:
                for page_number, titles in page_dict.items():
                    for title in titles:
                        try:
                            assert keyword.lower() in title.lower(), f"Title '{title}' on page {page_number} does not include the keyword '{keyword}'"
                        except AssertionError as ae:
                            issues.append(str(ae))

            return issues

        except Exception as e:
            logging.error(f"An error occurred during keyword checking: {str(e)}")
            return None  # Optionally, you can return None in case of an overall failure
            
    


    
       
            

            
            
        
            
        
        
        
         
 
        
        
    
    
    
    
    
    





    
    