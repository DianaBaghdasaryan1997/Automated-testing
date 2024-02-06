from selenium.webdriver.common.by import By
from Helper.general_helper import GeneralHelper
from Helper.json_parser import dump_to_json, parse_json
import logging
import json 

class RegisterPage(GeneralHelper):
    inp_first_name = (By.XPATH,"//div//input[@id='user[first_name]']")
    inp_last_name = (By.XPATH,"//div//input[@id='user[last_name]']")
    inp_email =  (By.XPATH,"//div//input[@id='user[email]']")
    inp_password =  (By.XPATH,"//div//input[@id='user[password]']")
    inp_user_terms = (By.XPATH,"//div//input[@id='user[terms]']")
    btn_sign_up = (By.XPATH, "//div//button[contains(text(),'Sign up')]")
    
    def register_account(self, name, surname, email, password):
        try:
            self.find_elem_and_send_data(self.inp_first_name, name)
            self.find_elem_and_send_data(self.inp_last_name, surname)
            self.find_elem_and_send_data(self.inp_email, email)
            self.find_elem_and_send_data(self.inp_password, password)
            self.find_and_click_elem(self.inp_user_terms)
            self.find_and_click_elem(self.btn_sign_up)
            config = parse_json(self.my_config)
            config['credentials']['email'] = email
            config['credentials']['password'] = password
            dump_to_json(config, self.my_config)
            logging.info(f'Registration successful for email: {email}')
        except Exception as e:
            logging.error(f'Registration failed for email {email }. Error: {str(e)}')
        
    
    
    

     
        
   
        