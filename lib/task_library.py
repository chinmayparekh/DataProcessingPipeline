import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import mysql.connector
import json


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def get_file_path(database_name):
    with open('config/config.json') as config_file:
        json_data = json.load(config_file)
  
        for db_entry in json_data["databases"]:
            if db_entry["database"] == database_name:
                return db_entry
        return None
    
def display(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()
        print(content)

        with open(output_file_path, 'w') as output_file:
            output_file.write(content)

def slice(input_file_path, output_file_path, column_name):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        df = pd.read_excel(input_file_path)
        sliced = df[column_name]

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(sliced))
    except FileNotFoundError:
        print("Error: Input file not found.")
    except KeyError:
        print("Error: Column not found in the DataFrame.")

# Function to dice a DataFrame by column names
def dice(input_file_path, output_file_path, column_names):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]

    try:
        print(column_names)
        df = pd.read_excel(input_file_path)
        diced = df[column_names]

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(diced))
    except FileNotFoundError:
        print("Error: Input file not found.")
    except KeyError:
        print("Error: Column not found in the DataFrame.")

# Function to remove null values from a DataFrame
def remove_nulls(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        df = pd.read_excel(input_file_path)
        no_nulls = df.dropna()

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(no_nulls))
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function to convert a column to uppercase in a DataFrame
def upper(input_file_path, output_file_path, column_name):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        df = pd.read_excel(input_file_path)
        df[column_name[0]] = df[column_name[0]].str.upper()

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(df))
    except FileNotFoundError:
        print("Error: Input file not found.")
    except KeyError:
        print("Error: Column not found in the DataFrame.")

# Function to calculate mean of a column in a DataFrame
def mean(input_file_path, output_file_path, column_name):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        df = pd.read_excel(input_file_path)
        mean_value = df[column_name].mean()

        with open(output_file_path, 'w') as output_file:
            output_file.write(str(mean_value))
    except FileNotFoundError:
        print("Error: Input file not found.")
    except KeyError:
        print("Error: Column not found in the DataFrame.")

# Function to convert text to uppercase
def uppercase(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        text = text.upper()
        
        with open(output_file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function to convert text to lowercase
def lowercase(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        text = text.lower()
        
        with open(output_file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function for tokenization
def tokenize_text(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        tokens = word_tokenize(text)
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(tokens))
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function for stemming
def stem_text(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        porter = PorterStemmer()
        tokens = word_tokenize(text)
        stemmed_tokens = [porter.stem(token) for token in tokens]
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(stemmed_tokens))
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function for lemmatization
def lemmatize_text(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(lemmatized_tokens))
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function for stopword removal
def remove_stopwords(input_file_path, output_file_path):
    input_file_path = get_file_path(input_file_path)["path"]
    output_file_path = get_file_path(output_file_path)["path"]
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()
        
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        
        with open(output_file_path, 'w') as file:
            file.write(' '.join(filtered_tokens))
    except FileNotFoundError:
        print("Error: Input file not found.")


def sql_connection(input_file_path, output_file_path):
    with open('config/config.json') as config_file:
        config = json.load(config_file)

    mydb = mysql.connector.connect(
        host = config['server'],
        user = config['user'],
        password = config['password'],
        database = config['database']
    )
    print(mydb)
    return mydb

import json
import mysql.connector

def sql_query(input_file_path, output_file_path, query):
    try:
        print("query: " + str(query[0]))

        with open('config/config.json') as config_file:
            config = json.load(config_file)
        
        mydb = mysql.connector.connect(
            host = config['server'],
            user = config['user'],
            password = config['password'],
            database = config['database']
        )
        cursor = mydb.cursor()

        cursor.execute(str(query[0]))

        rows = cursor.fetchall()

        with open(output_file_path, 'w') as output_file:
            for row in rows:
                output_file.write(str(row) + '\n')
                print(row)

        cursor.close()
        mydb.close()

    except FileNotFoundError:
        print("Error: Config file not found.")
    except mysql.connector.Error as db_error:
        print("MySQL Error:", db_error)
    except Exception as e:
        print("An error occurred:", str(e))
