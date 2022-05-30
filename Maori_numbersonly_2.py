import random 
import datetime
from datetime import time
import os



def rules():
    print('Welcome to the number quiz where you will learn to count from 1 to 50  in te reo')
    print('Here are the rules:')
    print('')
    print("1. Always enter the word for the number, the integer will not work")
    print('2. If you get a number correct three times in a row, you will not have to do it again.')
    print("3. You can press Q at anytime to go back to this menu")
    print('4. No cheating')

def welcome_screen():
    print('***********************************************')
    print('********************MENU***********************')
    print('***********************************************')
    print('')
    e = datetime.datetime.now()
    
    print('Kia Ora, Welcome')
    print (e.strftime("The time is %I:%M %p"))
    print('Press 1 for numbers from 1 to 10')
    print('Press 2 for numbers from 11 to 20')
    print('Press 3 for numbers from 21 to 30')
    print('Press 4 for numbers from 31 to 40')
    print('Press 5 for numbers from 41 to 50')
    user = int(input('Enter here:  '))
    while user != 4:
        if user == 1:
            numbers1_10()
        elif user == 2:
            numbers11_20()
        elif user == 3:
            numbers21_30()
        elif user == 4:
            numbers31_40()
        #elif user == 5:
            #numbers41_50()
        elif user == 'Q' or 'q':
            quit()
        else:
            print('Please enter a valid integer')



def numbers1_10():
    while 0 != 100:
        print('DIE PYTHON')

    os.abort()


welcome_screen()