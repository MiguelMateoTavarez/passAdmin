import os
import user
from getpass import getpass
from menu import menu

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