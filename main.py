#simple sign up and login system logic
# using try and except for good practice

try:
    username = input('Create Username: ')
    password = input('Create Password: ')
    print('Created account successfully')
    print('Now Try to Login Your account')

    createdUsername = input('Enter your username: ')
    createdPassword = input('Enter your password: ')

    if username == createdUsername and password == createdPassword:
        print('Login Succesfully')
    else:
        print('Invalid Credantials')
except:
    print('Unknown error accurs')