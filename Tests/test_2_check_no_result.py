from Pages.main import MainPage
from Pages.register import RegisterPage
from Pages.login import LoginPage
from Test_Data.test_data import *
from datetime import datetime
import logging

def test_2_check_no_result(driver):
    logging.info(f"Program has started at: {datetime.now()}")
    
    main_obj = MainPage(driver)
    register_obj = RegisterPage(driver)
    login_obj = LoginPage(driver)
    
    main_obj.navigate_to_url()
    main_obj.click_sign_in()
    login_obj.login_to_account()
    
    logging.info(f"Program has ended at: {datetime.now()}")
    
