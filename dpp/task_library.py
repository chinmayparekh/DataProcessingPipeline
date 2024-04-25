import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import mysql.connector
import json
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def get_file_path(database_name, config_path):
    with open(config_path) as config_file:
        json_data = json.load(config_file)
  
        for db_entry in json_data["databases"]:
            if db_entry["database"] == database_name:
                return db_entry
        logging.error('Could not find database')

def display(input_file_path, output_file_path, config_path):
    input_file_path = get_file_path(input_file_path, config_path)["path"]
    output_file_path = get_file_path(output_file_path,config_path)["path"]
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

        with open(output_file_path, 'w') as output_file:
            output_file.write(content)

def slice(input_file_path, output_file_path, column_name, config_path):
    try:
        logging.info("Slicing DataFrame")
        input_file_path = get_file_path(input_file_path, config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        df = pd.read_excel(input_file_path)
        sliced = df[column_name]

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(sliced))
    except FileNotFoundError:
        logging.error("Input file not found.")
    except KeyError:
        logging.error("Column not found in the DataFrame.")
    except TypeError as e:
        logging.error(f"Type error: {e}")

# Function to dice a DataFrame by column names
def dice(input_file_path, output_file_path, column_names,config_path):
    try:
        logging.info("Dicing DataFrame")
        input_file_path = get_file_path(input_file_path,config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        df = pd.read_excel(input_file_path)
        diced = df[column_names]

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(diced))
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except KeyError:
        logging.error("Column not found in the DataFrame.")
        #print("Error: Column not found in the DataFrame.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")

# Function to remove null values from a DataFrame
def remove_nulls(input_file_path, output_file_path,config_path):
    try:
        logging.info("Removing null values from DataFrame.")
        input_file_path = get_file_path(input_file_path,config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        df = pd.read_excel(input_file_path)
        no_nulls = df.dropna()

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(no_nulls))
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function to convert a column to uppercase in a DataFrame
def upper(input_file_path, output_file_path, column_name,config_path):
    try:
        logging.info("Converting column to uppercase: ")
        input_file_path = get_file_path(input_file_path,config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        df = pd.read_excel(input_file_path)
        df[column_name[0]] = df[column_name[0]].str.upper()

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(df))
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except KeyError:
        logging.error("Column not found in the DataFrame.")
        #print("Error: Column not found in the DataFrame.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function to calculate mean of a column in a DataFrame
def mean(input_file_path, output_file_path, column_name,config_path):
    try:
        logging.info("Calculating mean of column: ")
        input_file_path = get_file_path(input_file_path,config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        df = pd.read_excel(input_file_path)
        mean_value = df[column_name].mean()

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(mean_value))
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except KeyError:
        logging.error("Column not found in the DataFrame.")
        #print("Error: Column not found in the DataFrame.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function to convert text to uppercase
def uppercase(input_file_path, output_file_path,config_path):
    try:
        logging.info("Converting text to uppercase.")
        input_file_path = get_file_path(input_file_path,config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        text = text.upper()
        
        with open(output_file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function to convert text to lowercase
def lowercase(input_file_path, output_file_path,config_path):
    try:
        logging.info("Converting text to lowercase.")
        input_file_path = get_file_path(input_file_path,config_path)["path"]
        output_file_path = get_file_path(output_file_path,config_path)["path"]
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        text = text.lower()
        
        with open(output_file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        logging.error("Input file not found.")
        #print("Error: Input file not found.")
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function for tokenization
def tokenize_text(input_file_path, output_file_path,config_path):
    input_file_path = get_file_path(input_file_path,config_path)["path"]
    output_file_path = get_file_path(output_file_path,config_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        tokens = word_tokenize(text)
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(tokens))
        
        logging.info("Tokenization completed successfully for file: %s", input_file_path)
    except FileNotFoundError:
        logging.error("Input file not found: %s", input_file_path)
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function for stemming
def stem_text(input_file_path, output_file_path,config_path):
    input_file_path = get_file_path(input_file_path,config_path)["path"]
    output_file_path = get_file_path(output_file_path,config_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        porter = PorterStemmer()
        tokens = word_tokenize(text)
        stemmed_tokens = [porter.stem(token) for token in tokens]
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(stemmed_tokens))
        
        logging.info("Stemming completed successfully for file: %s", input_file_path)
    except FileNotFoundError:
        logging.error("Input file not found: %s", input_file_path)
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function for lemmatization
def lemmatize_text(input_file_path, output_file_path,config_path):
    input_file_path = get_file_path(input_file_path,config_path)["path"]
    output_file_path = get_file_path(output_file_path,config_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(lemmatized_tokens))
        
        logging.info("Lemmatization completed successfully for file: %s", input_file_path)
    except FileNotFoundError:
        logging.error("Input file not found: %s", input_file_path)
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")
# Function for stopword removal
def remove_stopwords(input_file_path, output_file_path,config_path):
    input_file_path = get_file_path(input_file_path,config_path)["path"]
    output_file_path = get_file_path(output_file_path,config_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(filtered_tokens))
        
        logging.info("Stopword removal completed successfully for file: %s", input_file_path)
    except FileNotFoundError:
        logging.error("Input file not found: %s", input_file_path)

    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")

def sql_query(input_file_path, output_file_path, query,config_path):
    # output_file_path = get_file_path(output_file_path,config_path)["path"]
    config = get_file_path(input_file_path,config_path)
    outputSQLTable = config['table']


    #print(input_file_path)
    try:

        mydb = mysql.connector.connect(
            host = config['server'],
            user = config['user'],
            password = config['password'],
            database = config['database']
        )
        cursor = mydb.cursor()
        print(get_file_path(output_file_path,config_path)["table"])
        cursor.execute(str(query[0]))
        logging.info("query: " + str(query))
        print(str(query[0]))
        rows = cursor.fetchall()
        num=len(rows[0])
        s_string = ','.join(['%s'] * num)
        print(s_string)
        for row in rows:
            # row = list(row)
            # row[0] = "BTV"
            # row[3]="122445678"
            # row = tuple(row)
            print(str(row))
            # print("INSERTING", row, "INTO", outputSQLTable)
            insert_query = f"INSERT INTO "+get_file_path(output_file_path,config_path)["table"]+" VALUES ("+s_string+")"  # Modify this query with your table's columns
            print(insert_query)
            cursor.execute(insert_query, row)


        # Commit the transaction
        mydb.commit()

        # with open(output_file_path, 'w') as output_file:
        #     for row in rows:
        #         output_file.write(str(row) + '\n')
                #print(row)

        cursor.close()
        mydb.close()

    except FileNotFoundError:
        logging.error("Config file not found")
    except mysql.connector.Error as db_error:
        logging.error("MySQL Error: %s", db_error)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
    except TypeError as e:
        logging.error(f"Type error: {e}")
        #print(f"Error: Type error - {e}")


