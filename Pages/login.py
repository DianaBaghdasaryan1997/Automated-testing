from selenium.webdriver.common.by import By
from Helper.general_helper import GeneralHelper
from Helper.json_parser import *
import logging

class LoginPage(GeneralHelper):
    link_create_account =  (By.XPATH,"//aside//a[contains(text(), 'Create a new account')]")
    inp_email =  (By.XPATH,"//div//input[@id='user[email]']")
    inp_password =  (By.XPATH,"//div//input[@id='user[password]']")
    btn_sign_in = (By.XPATH, "//div//button[contains(text(),'Sign in')]")
    
    def click_create_account(self):
        try:
            self.find_and_click_elem(self.link_create_account)
            logging.info('Navigating to the register page.')
        except Exception as e:
            logging.error(f'Failed to click "Create Account" link: {str(e)}')
            
    def login_to_account(self):
        try:
            config = parse_json(self.my_config)
            email = config['credentials']['email']
            password = config['credentials']['password']
            self.find_elem_and_send_data(self.inp_email, email)
            self.find_elem_and_send_data(self.inp_password, password)
            self.find_and_click_elem(self.btn_sign_in)
            self.driver.set_page_load_timeout(20)
            logging.info(f"Login successful for user:{email}")
            
        except Exception as e:
            logging.error(f"An error occurred during login: {e}")
        
        
        
        
            
    
    
            
    
    
    
