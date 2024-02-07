from Pages.main import MainPage
from Pages.register import RegisterPage
from Pages.login import LoginPage
from Test_Data.test_data import *
from datetime import datetime
import logging
import pytest 

@pytest.mark.parametrize("invalid_data", ['gbfgh'])
def test_2_check_no_result(driver, invalid_data):
    logging.info(f"Program has started at: {datetime.now()}")
    
    main_obj = MainPage(driver)
    register_obj = RegisterPage(driver)
    login_obj = LoginPage(driver)
    
    main_obj.navigate_to_url()
    main_obj.click_sign_in()
    login_obj.login_to_account()
    main_obj.search_data(invalid_data)
    result_text = main_obj.extract_elements_text(main_obj.loc_no_result)
    assert result_text[0] == "no results were found"
    logging.info(f"Program has ended at: {datetime.now()}")
    
