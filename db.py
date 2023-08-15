import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

database = mysql.connector.connect(
    host = os.environ.get('HOST'),
    user = os.environ.get('USER'),
    password = os.environ.get('PASSWRD')
)


#prepare cursour 

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE beauty')

print("Good job")