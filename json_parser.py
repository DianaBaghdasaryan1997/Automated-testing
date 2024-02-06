import logging 
import json

def parse_json(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            logging.info(f"Successfully parsed JSON from file: '{file_path}'")
            logging.debug(f"Parsed JSON data: {data}") 
            return data
    except FileNotFoundError:
        logging.error(f"File not found: '{file_path}'")
    except Exception as e:
        logging.error(f"An unexpected error occurred while parsing JSON from file '{file_path}'. Error: {str(e)}")
        
def dump_to_json(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)
            logging.info(f"Successfully dumped data to JSON file: '{file_path}'")
    except Exception as e:
        logging.error(f"An unexpected error occurred while dumping data to JSON file '{file_path}'. Error: {str(e)}")
