from selenium.webdriver.common.by import By
from Helper.general_helper import GeneralHelper
import logging

class Header(GeneralHelper):
    link_sign_in =  (By.XPATH,"//ul//li//a[contains(text(), 'Sign')]")
    
    def click_sign_in(self):
        try:
            self.find_and_click_elem(self.link_sign_in)
            logging.info('Navigating to Sign-In page.')
        except Exception as e:
            logging.error(f'Failed to click Sign-In link: {str(e)}')








