from multiprocessing import connection
from connection import *

def register(name, url, userName, password, description):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = '''INSERT INTO passwords (name, url, user_name, pass, description)
                    VALUES (?, ?, ?, ?, ?)'''
        dates = (name, url, userName, password, description)
        cursor.execute(query, dates)
        connection.commit()
        connection.close()
        
        return 'It has been successfully registered'
    except Error as err:
        return 'An error has occurred ' + str(err)

def show():
    dates = []
    try:
        connection = connect()
        cursor = connection.cursor()
        query = '''SELECT * FROM passwords'''
        cursor.execute(query)
        dates = cursor.fetchall()
        connection.close()
    except Error as err:
        print('An error has occurred ' + str(err))
    
    return dates

def find(id):
    dates = []
    try:
        connection = connect()
        cursor = connection.cursor()
        query = '''SELECT * FROM passwords WHERE id = ?'''
        cursor.execute(query, (id,))
        dates = cursor.fetchall()
        connection.close()
    except Error as err:
        print('An error has occurred ' + str(err))
    
    return dates

def modify(id, name, url, userName, password, description):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = '''UPDATE passwords SET name = ?, url = ?, user_name = ?, pass = ?, description = ? WHERE id = ?'''
        dates = (name, url, userName, password, description, id)
        cursor.execute(query, dates)
        connection.commit()
        connection.close()

        return 'The password has been changed'

    except Error as err:
        return 'An error has occurred '+ str(err)

def delete(id):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = 'DELETE FROM passwords WHERE id = ?'
        cursor.execute(query, (id,))
        connection.commit()
        connection.close()

        return 'The password has been deleted'
    except Error as err:
        return 'An error has occurred '+ str(err)