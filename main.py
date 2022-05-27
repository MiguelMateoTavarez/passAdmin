import os
from getpass import getpass
from pydoc import describe
from tabulate import tabulate #Importado con pip install tabulate
from connection import *
import user
from user import *

connection = connect()
createTables(connection)

def start():
    os.system('cls')
    validate = user.validateUser()
    if len(validate) == 0:
        print('Welcome, login please')
        name = input('Name: ')
        lastName = input('Lastname: ')
        masterPass = getpass('Password: ')

        result = user.register(name, lastName, masterPass)

        if result == 'Register successfuly':
            print(f'Welcome {name}')
            menu()
        else:
            print(result)
    else:
        masterPass = getpass('Password: ')
        result = user.validatePassword(1, masterPass)
        if len(result) == 0:
            print('Wrong id or password')
        else:
            print('Welcome!')
            menu()

def menu():
    while True:
        print('Choose one of the following options: ')
        print('\t1- Add password')
        print('\t2- Show all the passwords')
        print('\t3- Whatch a password')
        print('\t4- Modify a password')
        print('\t5- Delete a password')
        print('\t6- Exit')
        option = input('Please enter an option: ')

        if option == '1':
            newPassword()
        elif option == '2':
            print('Showing a passwords')
        elif option == '3':
            print('Watching a password')
        elif option == '4':
            print('Modifying a password')
        elif option == '5':
            print('Deleting a password')
        elif option == '6':
            break
        else:
            print('You did not enter a valid option')

def newPassword():
    name = input('Name: ')
    url = input('Url: ')
    userName = input('Username: ')
    password = input('Pass: ')
    description = input ('Descrition')

    result = password.register(name, url, userName, password, description)
    print(result)
start()