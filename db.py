import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Bimbo4wife'
)


#prepare cursour 

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE beauty')

print("Good job")