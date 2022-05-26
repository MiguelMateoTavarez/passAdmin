import os
from getpass import getpass
from tabulate import tabulate #Importado con pip install tabulate
from connection import *

connection = connect()
createTables(connection)

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
            print('Adding a password')
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

menu()