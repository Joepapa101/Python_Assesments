import random
from re import S
import time
import datetime

def rules():
    print('Welcome to the number quiz where you will learn to count from 1 to 50  in te reo')
    print('Here are the rules:')
    print('')
    print("1. Always enter the word for the number, the integer will not work")
    print('2. If you get a number correct three times in a row, you will not have to do it again.')
    print("3. You can press Q at anytime to go back to this menu")
    print('4. No cheating')
    print('5. Enter the number like this:  Wha tekau ma rima, sixty five')
    print('6. No macrons required')
    welcome_screen()

def welcome_screen():
    print('***********************************************')
    print('********************MENU***********************')
    print('***********************************************')
    print('')
    #time variable
    e = datetime.datetime.now()
    print('Kia Ora, Welcome')
    #print the time
    print (e.strftime("The time is %I:%M %p"))
    print('Press 1 for numbers from 1 to 10')
    print('Press 2 for numbers from 11 to 20')
    print('Press 3 for numbers from 21 to 30')
    print('Press 4 for numbers from 31 to 40')
    print('Press 5 for numbers from 41 to 50')
    print('Press 6 for the rules')
    print('Press 7 for the numbers and their translations')
    print('Press 0 to quit the program')
    
    while 0 != 100:
        user = int(input('Enter here:  '))
        if user == 1:
            numbers1_10()
        elif user == 2:
            numbers11_20()
        elif user == 3:
            numbers21_30()
        elif user == 4:
            numbers31_40()
        elif user == 5:
            numbers41_50()
        elif user == 6:
            rules()
        elif user == 7:
            number_lists()
        elif user == 0:
            quit()
        else:
            print('Please enter a valid integer')




def numbers1_10():
    #variables
    counter = 9
    list_counter = 1
    numbers = []
    answers_words = []
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    english1_10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    maori1_10 = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    #if 1 is pressed it will go to the maori to english translation, vice versa if 2 is pressed
    print('Welcome to the m??ori number quiz from 11-20')
    print('Press 1 if you want the m??ori question and for you to answer in english')
    print('Press 2 if you want the english question and for you to answer in m??ori')
    decider = int(input('Enter option:  '))
    if decider == 1:
        numbers = maori1_10
        answers_words = english1_10
    elif decider == 2:
        numbers = english1_10
        answers_words = maori1_10
    else:
        print('Please enter a valid integer')
    #while the counter variable isn't 0, this will keep looping
    while counter != 0:
        #random number generator
        answer_generator = random.randint(0, counter)
        #the question and answer will be generated by the generator
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        #the user asks the question h
        user = input('Enter english answer:  ')
        #if the user's answer matches up with the variable answer, the program will print it as 'correct' otherwise it will print it as 'wrong'
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            print('')
            if times_answered[answer_generator] == 3:
                numbers.remove(question)
                answers_words.remove(answer)
                times_answered.remove(3)         
                counter -= 1
                print('')
        elif user != answer:
            print(f'{question} is actually {answer} ')
            print('')
            time.sleep(2)

    print('')
    print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')
    print('')
    welcome_screen()







def numbers11_20():
    #variables
    counter = 9
    list_counter = 1
    numbers = []
    answers_words = []
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    english11_20 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    maori11_20 = ['tekau ma tahi', 'tekau ma rua', 'tekau ma toru', 'tekau ma wha', 'tekau ma rima', 'tekau ma ono', 'tekau ma whitu', 'tekau ma waru', 'tekau ma iwa', 'rua tekau']
    #if 1 is pressed it will go to the maori to english translation, vice versa if 2 is pressed
    print('Welcome to the m??ori number quiz from 11-20')
    print('Press 1 if you want the m??ori question and for you to answer in english')
    print('Press 2 if you want the english question and for you to answer in m??ori')
    decider = int(input('Enter option:  '))
    if decider == 1:
        numbers = maori11_20
        answers_words = english11_20
    elif decider == 2:
        numbers = english11_20
        answers_words = maori11_20
    else:
        print('Please enter a valid integer')
    #while the counter variable isn't 0, this will keep looping
    while counter != 0:
        #random number generator
        answer_generator = random.randint(0, counter)
        #the question and answer will be generated by the generator
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        #the user asks the question h
        user = input('Enter english answer:  ')
        #if the user's answer matches up with the variable answer, the program will print it as 'correct' otherwise it will print it as 'wrong'
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            print('')
            if times_answered[answer_generator] == 3:
                numbers.remove(question)
                answers_words.remove(answer)
                times_answered.remove(3)         
                counter -= 1
                print('')
        elif user != answer:
            print(f'{question} is actually {answer} ')
            print('')
            time.sleep(2)

    print('')
    print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')
    print('')
    welcome_screen()



def numbers21_30():
    #variables
    counter = 9
    list_counter = 1
    numbers = []
    answers_words = []
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    english21_30 = ['twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'thirty']
    maori21_30 = ['rua tekau ma tahi', 'rua tekau ma rua', 'rua tekau ma toru', 'rua tekau ma wha', 'rua tekau ma rima', 'rua tekau ma ono', 'rua tekau ma whitu', 'rua tekau ma waru', 'rua tekau ma iwa', 'toru tekau']
    #if 1 is pressed it will go to the maori to english translation, vice versa if 2 is pressed
    print('Welcome to the m??ori number quiz from 11-20')
    print('Press 1 if you want the m??ori question and for you to answer in english')
    print('Press 2 if you want the english question and for you to answer in m??ori')
    decider = int(input('Enter option:  '))
    if decider == 1:
        numbers = maori21_30
        answers_words = english21_30
    elif decider == 2:
        numbers = english21_30
        answers_words = maori21_30
    else:
        print('Please enter a valid integer')
    #while the counter variable isn't 0, this will keep looping
    while counter != 0:
        #random number generator
        answer_generator = random.randint(0, counter)
        #the question and answer will be generated by the generator
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        #the user asks the question h
        user = input('Enter english answer:  ')
        #if the user's answer matches up with the variable answer, the program will print it as 'correct' otherwise it will print it as 'wrong'
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            print('')
            if times_answered[answer_generator] == 3:
                numbers.remove(question)
                answers_words.remove(answer)
                times_answered.remove(3)         
                counter -= 1
                print('')
        elif user != answer:
            print(f'{question} is actually {answer} ')
            print('')
            time.sleep(2)

    print('')
    print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')
    print('')
    welcome_screen()



def numbers31_40():
    #variables
    counter = 9
    list_counter = 1
    numbers = []
    answers_words = []
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    english31_40 = ['thirty one', 'thirty two', 'thirty three', 'thirty four', 'thirty five', 'thirty six', 'thirty seven', 'thirty eight', 'thirty nine', 'fourty']
    maori31_40 = ['toru tekau ma tahi', 'toru tekau ma rua', 'toru tekau ma toru', 'toru tekau ma wha', 'toru tekau ma rima', 'toru tekau ma ono', 'toru tekau ma whitu', 'toru tekau ma waru', 'toru tekau ma iwa', 'wha tekau']
    #if 1 is pressed it will go to the maori to english translation, vice versa if 2 is pressed
    print('Welcome to the m??ori number quiz from 11-20')
    print('Press 1 if you want the m??ori question and for you to answer in english')
    print('Press 2 if you want the english question and for you to answer in m??ori')
    decider = int(input('Enter option:  '))
    if decider == 1:
        numbers = maori31_40
        answers_words = english31_40
    elif decider == 2:
        numbers = english31_40
        answers_words = maori31_40
    else:
        print('Please enter a valid integer')
    #while the counter variable isn't 0, this will keep looping
    while counter != 0:
        #random number generator
        answer_generator = random.randint(0, counter)
        #the question and answer will be generated by the generator
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        #the user asks the question h
        user = input('Enter english answer:  ')
        #if the user's answer matches up with the variable answer, the program will print it as 'correct' otherwise it will print it as 'wrong'
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            print('')
            if times_answered[answer_generator] == 3:
                numbers.remove(question)
                answers_words.remove(answer)
                times_answered.remove(3)         
                counter -= 1
                print('')
        elif user != answer:
            print(f'{question} is actually {answer} ')
            print('')
            time.sleep(2)

    print('')
    print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')
    print('')
    welcome_screen()


def numbers41_50():
    #variables
    counter = 9
    list_counter = 1
    numbers = []
    answers_words = []
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    english41_50 = ['fourty one', 'fourty two', 'fourty three', 'fourty four', 'fourty five', 'fourty six', 'fourty seven', 'fourty eight', 'fourty nine', 'fifty']
    maori41_50 = ['wha tekau ma tahi', 'wha tekau ma rua', 'wha tekau ma toru', 'wha tekau ma wha', 'wha tekau ma rima', 'wha tekau ma ono', 'wha tekau ma whitu', 'wha tekau ma waru', 'wha tekau ma iwa', 'rima tekau']
    #if 1 is pressed it will go to the maori to english translation, vice versa if 2 is pressed
    print('Welcome to the m??ori number quiz from 11-20')
    print('Press 1 if you want the m??ori question and for you to answer in english')
    print('Press 2 if you want the english question and for you to answer in m??ori')
    decider = int(input('Enter option:  '))
    if decider == 1:
        numbers = maori41_50
        answers_words = english41_50
    elif decider == 2:
        numbers = english41_50
        answers_words = maori41_50
    else:
        print('Please enter a valid integer')
    #while the counter variable isn't 0, this will keep looping
    while counter != 0:
        #random number generator
        answer_generator = random.randint(0, counter)
        #the question and answer will be generated by the generator
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        #the user asks the question h
        user = input('Enter english answer:  ')
        #if the user's answer matches up with the variable answer, the program will print it as 'correct' otherwise it will print it as 'wrong'
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            print('')
            if times_answered[answer_generator] == 3:
                numbers.remove(question)
                answers_words.remove(answer)
                times_answered.remove(3)         
                counter -= 1
                print('')
        elif user != answer:
            print(f'{question} is actually {answer} ')
            print('')
            time.sleep(2)

    print('')
    print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')
    print('')
    welcome_screen()



def number_lists():
    #list from 1-10
    english1_10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    maori1_10 = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    #list from 11-20
    english11_20 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    maori11_20 = ['tekau ma tahi', 'tekau ma rua', 'tekau ma toru', 'tekau ma wha', 'tekau ma rima', 'tekau ma ono', 'tekau ma whitu', 'tekau ma waru', 'tekau ma iwa', 'rua tekau']
    #list from 21-30
    english21_30 = ['twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'thirty']
    maori21_30 = ['rua tekau ma tahi', 'rua tekau ma rua', 'rua tekau ma toru', 'rua tekau ma wha', 'rua tekau ma rima', 'rua tekau ma ono', 'rua tekau ma whitu', 'rua tekau ma waru', 'rua tekau ma iwa', 'toru tekau']
    #list from 31-40
    english31_40 = ['thirty one', 'thirty two', 'thirty three', 'thirty four', 'thirty five', 'thirty six', 'thirty seven', 'thirty eight', 'thirty nine', 'fourty']
    maori31_40 = ['toru tekau ma tahi', 'toru tekau ma rua', 'toru tekau ma toru', 'toru tekau ma wha', 'toru tekau ma rima', 'toru tekau ma ono', 'toru tekau ma whitu', 'toru tekau ma waru', 'toru tekau ma iwa', 'wha tekau']
    #list from 41-50
    english41_50 = ['fourty one', 'fourty two', 'fourty three', 'fourty four', 'fourty five', 'fourty six', 'fourty seven', 'fourty eight', 'fourty nine', 'fifty']
    maori41_50 = ['wha tekau ma tahi', 'wha tekau ma rua', 'wha tekau ma toru', 'wha tekau ma wha', 'wha tekau ma rima', 'wha tekau ma ono', 'wha tekau ma whitu', 'wha tekau ma waru', 'wha tekau ma iwa', 'rima tekau']
    print('Press 1 for numbers 1-10 and their translations')
    print('Press 2 for numbers 11-20 and their translations')
    print('Press 3 for number 21-30 and their tranlations')
    print('Press 4 for numbers 31-40 and their tranlstions')
    print('Press 5 for numbers 41-50 and their translations')
    print('Press 6 to go back to the main menu')
    #this will keep the loop running until the user decides to go back to the main menu
    while 0 != 100:
        userinput = int(input('Enter here:  '))
        #if the user input is 'X', print the numbers from 'X' to 'Y' in english and maori
        if userinput == 1:
            print(english1_10)
            print(maori1_10)
        elif userinput == 2:
            print(english11_20)
            print(maori11_20)
        elif userinput == 3:
            print(english21_30)
            print(maori21_30)
        elif userinput == 4:
            print(english31_40)
            print(maori31_40)
        elif userinput == 5:
            print(english41_50)
            print(maori41_50)
        elif userinput == 6:
            welcome_screen()
        else:
            print('Enter a valid integer')










#main routine
welcome_screen()