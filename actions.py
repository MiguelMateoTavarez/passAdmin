import password
import user
from getpass import getpass
from tabulate import tabulate

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
