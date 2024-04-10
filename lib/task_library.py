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

def display(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()
        print(content)

        with open(output_file_path, 'w') as output_file:
            output_file.write(content)

def slice(input_file_path, output_file_path, column_name):
    df = pd.read_excel(input_file_path)
    sliced = df[column_name]

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(sliced))

def dice(input_file_path, output_file_path, column_names):
    print(column_names)
    df = pd.read_excel(input_file_path)
    diced = df[column_names]

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(diced))

def remove_nulls(input_file_path, output_file_path):
    df = pd.read_excel(input_file_path)
    no_nulls = df.dropna()

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(no_nulls))

def upper(input_file_path, output_file_path, column_name):
    df = pd.read_excel(input_file_path)
    df[column_name[0]] = df[column_name[0]].str.upper()

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(df))

def mean(input_file_path, output_file_path, column_name):
    df = pd.read_excel(input_file_path)
    mean = df[column_name].mean()

    with open(output_file_path, 'w') as output_file:
        output_file.write(str(mean))



def uppercase(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    text = text.upper()
    
    with open(output_file_path, 'w') as file:
        file.write(text)

# Function to convert text to lowercase
def lowercase(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    text = text.lower()
    
    with open(output_file_path, 'w') as file:
        file.write(text)

# Function for tokenization
def tokenize_text(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    tokens = word_tokenize(text)
    
    with open(output_file_path, 'w') as file:
        file.write(' '.join(tokens))

# Function for stemming
def stem_text(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    porter = PorterStemmer()
    tokens = word_tokenize(text)
    stemmed_tokens = [porter.stem(token) for token in tokens]
    
    with open(output_file_path, 'w') as file:
        file.write(' '.join(stemmed_tokens))

# Function for lemmatization
def lemmatize_text(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    with open(output_file_path, 'w') as file:
        file.write(' '.join(lemmatized_tokens))

# Function for stopword removal
def remove_stopwords(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
    with open(output_file_path, 'w') as file:
        file.write(' '.join(filtered_tokens))

def sql_connection():
    with open('config/config.json') as config_file:
        config = json.load(config_file)

    mydb = mysql.connector.connect(
        host = config['server'],
        user = config['user'],
        password = config['password'],
        database = config['database']
    )

    return mydb

def sql_query(query, mydb):
    cursor = mydb.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    mydb.close()

sql_query("SELECT * FROM employee", sql_connection())