import os
from getpass import getpass
from pydoc import describe
from tabulate import tabulate #Importado con pip install tabulate
from connection import *
import user
import password

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

        if result == 'It has been successfully registered':
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
            showPasswords()
        elif option == '3':
            findPassword()
        elif option == '4':
            modifyPassword()
        elif option == '5':
            deletePassword()
        elif option == '6':
            break
        else:
            print('You did not enter a valid option')

def newPassword():
    name = input('Name: ')
    url = input('Url: ')
    userName = input('Username: ')
    passw = input('Pass: ')
    description = input ('Descrition: ')

    result = password.register(name, url, userName, passw, description)
    print(result)

def showPasswords():
    dates = password.show()
    newDates = []
    headers = ['ID', 'NAME', 'URL', 'USER', 'PASSWORD', 'DESCRIPTION']
    for date in dates:
        switch = list(date)
        switch[4] = '************'
        newDates.append(switch)
    table = tabulate(newDates, headers, tablefmt='fancy_grid')
    print('\t\t\t\tAll passwords')
    print(table)

def findPassword():
    masterPass = getpass('Password: ')
    response = user.validatePassword(1, masterPass)
    if (len(response)) == 0:
        print('Worng password')
    else:
        id = input('Enter the key id to search: ')
        dates = password.find(id)
        headers = ['ID', 'NAME', 'URL', 'USER', 'PASSWORD', 'DESCRIPTION']
        table = tabulate(dates, headers, tablefmt='fancy_grid')
        print('\t\t\t\tAll passwords')
        print(table)

def modifyPassword():
    masterPass = getpass('Password: ')
    response = user.validatePassword(1, masterPass)
    if (len(response)) == 0:
        print('Worng password')
    else:
        id = input('Enter the key id to edit: ')
        name = input('New name: ')
        url = input('New url: ')
        userName = input('New username: ')
        passw = input('New pass: ')
        description = input('New description: ')
        responde = password.modify(id, name, url, userName, passw, description)
        print(responde)

def deletePassword():
    masterPass = getpass('Password: ')
    response = user.validatePassword(1, masterPass)
    if (len(response)) == 0:
        print('Worng password')
    else:
        id = input('Enter the key id to delete: ')
        response = password.delete(id)
        print(response)

start()