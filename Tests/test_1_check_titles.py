from Pages.main import MainPage
from Pages.register import RegisterPage
from Pages.login import LoginPage
from Test_Data.test_data import *
from datetime import datetime
import logging
import os
import time
import pytest 

@pytest.mark.parametrize("valid_data", ['selenium'])
def test_check_titles(driver, valid_data):
    logging.info(f"Program has started at: {datetime.now()}")
    
    main_obj = MainPage(driver)
    register_obj = RegisterPage(driver)
    login_obj = LoginPage(driver)
    
    main_obj.navigate_to_url()
    main_obj.click_sign_in()
    login_obj.click_create_account()
    register_obj.register_account(credentials['firstname'], credentials['lastname'],
                                  credentials['email'], credentials['password']
                                 )
    final_text  = main_obj.get_titles(valid_data) 
    logging.info(final_text )
    
    logging.info(f"Program has ended at: {datetime.now()}")
    
