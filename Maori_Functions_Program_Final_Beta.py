import random
import datetime
import time



def welcome_options():
    date_time = datetime.datetime.now
    print('*********************************************')
    print('******************MAIN MENU******************')
    print('*********************************************')    
    print('')
    print('Kia Ora, Welcome')
    #print("The time is now: = %s:%s:%s" % (date_time.hour, date_time.minute, date_time.second))
    print('')
    print('Māori Quiz Options:')
    print('')
    print('Type 1 for the number quiz')
    print('Type 2 for the month quiz ')
    print('Type 3 for the days of the week quiz')
    print('Type 0 to exit')
    print()
    options = 0
    while options != 4:
        options = int(input('Enter here:  '))
        if options == 1:
            print('')
            number_quiz()
        elif options == 2:
            month_quiz()
        #elif options == 3:
            #daysoftheweekquiz
        #elif options == 0:
            #exit
        else:
            print('Enter a valid integer')
        







def number_quiz():
    print('Welcome to the number quiz where you will learn to count from one to ten in te reo')
    print('')
    print('Here are the rules:  ')
    print("1. Always enter the word for the number, the integer will not work")
    print('2. If you get a number correct three times in a row, you will not have to do it again.')
    print("3. You can press Q at anytime to go back to this menu")
    print('4. No cheating')
    print('')
    print('')
    print('Type 1 for the numbers and their translations in te reo')
    print('Type 2 to go to the māori to english numbers quiz')
    print('Type 3 to go to the english to māori numbers quiz')
    print('Type 4 to go back to the main menu')
    print('')
    userinput = 0
    userinput = int(input('Enter here:  '))
    while userinput != 4:
        if userinput == 1:
            print('')
            number_quiz_numbers()
        elif userinput == 2:
            number_quiz_maori_english()
        elif userinput == 3:
            number_quiz_english_maori()
        elif userinput == 4:
            welcome_options()


#Option-1
def number_quiz_numbers():
    maori = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    english = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    print(maori)
    print(english)
    print('')
    time.sleep(3)
    user = input('Press ENTER to go back to the menu')
    if user == '':
        number_quiz()
    else:
        number_quiz()


def number_quiz_maori_english():
    error_checker = 0
    counter = 9
    numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    answers_words = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while counter != 0:
        answer_generator = random.randint(0, counter)
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        user = input('Enter english answer:  ')
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            error_checker += 1
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
        elif user == 'q' or 'Q':
            print('too bad')
    




#Option-3
def number_quiz_english_maori():
    error_checker = 0
    counter = 9
    numbers = ['Tahi', 'Rua', 'Toru', 'Wha', 'Rima', 'Ono', 'Whitu', 'Waru', 'Iwa', 'Tekau']
    answers_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while counter != 0:
        answer_generator = random.randint(0, counter)
        question = numbers[answer_generator]
        answer = answers_words[answer_generator]
        print(question)
        user = input('Enter english answer:  ')
        if user == answer:
            print('Correct')
            times_answered[answer_generator] += 1
            error_checker += 1
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
        elif user == 'q' or 'Q':
            print('too bad')



print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')



def month_quiz():
    print('')
    print('Welcome to the month quiz!')
    print('Here are the rules: ')
    print('1. You can get the translations😘 by pressing 1')
    print('2. If you get a month correct three times in a row, you will not have to do it again')
    print('3. You can press Q to quit at any time')
    print('')
    print('')
    print('Type 1 for the months and their translations in te reo Māori')
    print('Type 2 for the month quiz from māori to english')
    print('Type 3 for the month quiz from english to māori')
    print('Type 4 to go back to the main menu')
    print('')
    userinput1 = int(input('Enter here:  '))
    while userinput1 != 4:
        if userinput1 == 1:
            month_quiz_translations()
        elif userinput1 == 2:
            month_quiz_maori_english()
        #elif userinput1 == 3:
            #month_quiz_english_maori()
        elif userinput1 == 4:
            welcome_options()
        else:
            print('Please enter a valid integer')



def month_quiz_translations():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_answers = ['Hanuere', 'Pepuere', 'Maehe', 'Aperera', 'Mei', 'Hune', 'Hurae', 'Akuhata', 'Hepetema', 'Okitopa', 'Noema', 'Tihema']
    months_answers2 = ['Kohitatea', 'Hui-Tangaru', 'Poutu-te-rangi', 'Paenga-whawha', 'Haratua', 'Pipiri', 'Hongongoi', 'Here-tui-koka', 'Mahuru', 'Whiringa-nuku', 'Whiringa-rangi', 'Hakihea']
    print(months)
    print(months_answers)
    print(months_answers2)
    time.sleep(2)
    enteruser = input('Press ENTER to go back to the months menu')
    if enteruser == '':
        month_quiz()
    else:
        month_quiz()



def month_quiz_maori_english():
    difficuilty = int(input('Enter on a scale of 1 to 3 how many of the months you know already, 1 being no experience:  '))
    counter = 12


    print('')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_answers = ['Hanuere', 'Pepuere', 'Maehe', 'Aperera', 'Mei', 'Hune', 'Hurae', 'Akuhata', 'Hepetema', 'Okitopa', 'Noema', 'Tihema']
    months_answers2 = ['Kohitatea', 'Hui-Tangaru', 'Poutu-te-rangi', 'Paenga-whawha', 'Haratua', 'Pipiri', 'Hongongoi', 'Here-tui-koka', 'Mahuru', 'Whiringa-nuku', 'Whiringa-rangi', 'Hakihea']
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while counter != 0:
        answer_generator = random.randint(0, counter)
        question = months[answer_generator]
        answer = months_answers[answer_generator]
        answer2 = months_answers2[answer_generator]
        print(question)
        user = input('Enter english answer:  ')
        if user == answer or user == answer2:
            print('Correct')
            times_answered[answer_generator] += 1
            print(times_answered)
            print('')
            if times_answered[answer_generator] == 3:
                counter -= 1
                months.remove(question)
                months_answers.remove(answer)
                months_answers2.remove(answer)
                times_answered.remove[answer_generator]
                print(times_answered)
                print('')
        elif user != answer:
            print(f'{question} is actually {answer} or {answer2} ')
            print('')
            time.sleep(2)
        elif user == 'q' or 'Q':
            print('too bad')

    





#main routine
welcome_options()








