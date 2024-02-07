from Pages.main import MainPage
from Pages.register import RegisterPage
from Pages.login import SignInPage
from Test_Data.test_data import *
from datetime import datetime
import logging

def test_check_product(driver):
    logging.info(f"Program has started at: {datetime.now()}")

    main_obj = MainPage(driver)
    register_obj = RegisterPage(driver)
    login_obj = SignInPage(driver)
    
    main_obj.navigate_to_url()
  

    logging.info(f"Program has ended at: {datetime.now()}")

