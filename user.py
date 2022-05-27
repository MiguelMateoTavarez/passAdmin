import hashlib
from connection import *

def validateUser():
    connection = connect()
    cursor = connection.cursor()
    query = 'SELECT * FROM users'
    cursor.execute(query)
    user_findef = cursor.fetchall()
    connection.close()

    return user_findef;

def register(name, lastName, masterPass):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = '''INSERT INTO users (name, last_name, master_pass) VALUES (?, ?, ?)'''
        passHashed = hashlib.sha256(masterPass.encode('utf-8')).hexdigest()
        dates = (name, lastName, passHashed)
        cursor.execute(query, dates)
        connection.commit()
        connection.close()

        return 'Register successfuly'
    except Error as err:
        return 'Ha ocurridlo un error ' + str(err)

def validatePassword(id, masterPass):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = '''SELECT * FROM users WHERE id = ? AND master_pass = ?'''
        passHashed = hashlib.sha256(masterPass.encode('utf-8')).hexdigest()
        cursor.execute(query, (id, passHashed))
        dates = cursor.fetchall()
        cursor.close()

        return dates
    except Error as err:
        return 'Ha ocurrido un error ' + str(err)