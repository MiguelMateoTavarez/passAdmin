import sqlite3
from sqlite3 import Error

def connect():
    try:
        connection = sqlite3.connect('passadmin.db')
        return connection
    except Error as err:
        print('Ha ocurrido un error')

def createTables(connection):
    cursor = connection.cursor()
    first_query = '''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        master_pass TEXT NOT NULL
    )'''
    second_query = '''CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT NOT NULL,
        user_name TEXT NOT NULL,
        pass TEXT NOT NULL,
        description TEXT
    )'''

    cursor.execute(first_query)
    cursor.execute(second_query)
    connection.commit()
    connection.close()