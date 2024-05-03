import json
import logging
from dpp import task_library
import pandas as pd





def slice(input_file_path, output_file_path, column_name,config_path):
    a=0
    for i in range(0, 100000000):
        a+=1
    try:
        logging.info("Slicing DataFrame")
        input_file_path = task_library.get_file_path(input_file_path,config_path)["path"]
        output_file_path = task_library.get_file_path(output_file_path,config_path)["path"]
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