from Pages.header import Header
from Pages.main import MainPage
from Pages.register import RegisterPage
from Pages.login import LoginPage
from Test_Data.test_data import *
from datetime import datetime
import logging
import os
import time

def test_search_valid(driver):
    logging.info(f"Program has started at: {datetime.now()}")
    
    header_obj = Header(driver)
    main_obj = MainPage(driver)
    register_obj = RegisterPage(driver)
    login_obj = LoginPage(driver)
    
    main_obj.navigate_to_url()
    header_obj.click_sign_in()
    login_obj.create_account()
    register_obj.register_account(credentials['firstname'], credentials['lastname'],
                                  credentials['email'],credentials['password']
                                 )
    
    logging.info(f"Program has ended at: {datetime.now()}")

