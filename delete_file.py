from selenium.webdriver.support import expected_conditions as EC
import logging
import os

def delete_file(file_name):
    try:
        file_path = os.path.join(os.path.dirname(__file__), file_name)

        if os.path.exists(file_path):
            confirm = input(f"Do you want to remove '{file_name}' file? (yes/no): ")

            if confirm.lower() == "yes":
                os.remove(file_path)
                logging.info(f"'{file_name}' file has been deleted.")
            elif confirm.lower() == "no":
                logging.info(f"'{file_name}' file hasn't been deleted.")
            else:
                logging.warning(f"'{file_name}' file hasn't been deleted due to incorrect input.")
        else:
            logging.info(f"'{file_name}' file doesn't exist.")

    except Exception as e:
        logging.error(f"Error occurred while deleting '{file_name}' file. Exception: {e}")
    
        