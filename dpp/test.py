import mysql.connector
import json

with open('config/config.json') as config_file:
    config = json.load(config_file)

# Creating connection object
mydb = mysql.connector.connect(
    host = config['server'],
    user = config['user'],
    password = config['password'],
    database = config['database']
)

cursor = mydb.cursor()

query = "SELECT * FROM employee"  
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
mydb.close()

print(mydb)
