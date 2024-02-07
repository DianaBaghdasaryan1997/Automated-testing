import pytest
import logging
import os
from selenium import webdriver

@pytest.fixture
def driver():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as error:
        raise Exception(error)

def pytest_configure():
    logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename=os.path.join(os.path.dirname(__file__), "my_logs.log"),
                    filemode='a',
                    encoding='utf-8'
                    )