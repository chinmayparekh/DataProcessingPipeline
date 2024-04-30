import json
import logging

import pandas as pd


def get_file_path(database_name):
    with open('config/config.json') as config_file:
        json_data = json.load(config_file)
  
        for db_entry in json_data["databases"]:
            if db_entry["database"] == database_name:
                return db_entry
        logging.error('Could not find database')


def slice(input_file_path, output_file_path, column_name):
    try:
        logging.info("Slicing DataFrame")
        input_file_path = get_file_path(input_file_path)["path"]
        output_file_path = get_file_path(output_file_path)["path"]
        df = pd.read_excel(input_file_path)
        sliced = df[column_name]

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(sliced))
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except KeyError:
        logging.error("Column not found in the DataFrame.")
        #print("Error: Column not found in the DataFrame.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")