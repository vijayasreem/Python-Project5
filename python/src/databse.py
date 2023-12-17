import sqlite3
import os

script_dir = os.path.dirname(__file__)
database_path = os.path.join(script_dir, '../db/db.sql')

try:
    conn = sqlite3.connect(database_path)
    print("Connected to Database")
except sqlite3.Error as e:
    print("Error connecting to Database")
    print(e)
