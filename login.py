from selenium.webdriver.common.by import By
from Helper.general_helper import GeneralHelper
import logging

class LoginPage(GeneralHelper):
    link_create_account =  (By.XPATH,"//aside//a[contains(text(), 'Create a new account')]")
    inp_email =  (By.XPATH,"//input[@id='ap_password']")
    inp_password =  (By.XPATH,"//input[@id='ap_password']")
    btn_sign_in = (By.XPATH, "//div//button[contains(text(),'Sign in')]")
    
    def create_account(self):
        try:
            self.find_and_click_elem(self.link_create_account)
            logging.info('Navigating to the register page.')
        except Exception as e:
            logging.error(f'Failed to click "Create Account" link: {str(e)}')
            
    
    
            
    
    
    
