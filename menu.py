from actions import *

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