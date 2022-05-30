import random


def welcome_options():
    print('Māori Quiz Options:')
    print('')
    print('Type 1 for the number quiz')
    print('Type 2 for the month quiz ')
    print('Type 3 for the days of the week quiz')
    print('Type 0 to exit')
    print()
    options = int(input('Enter here:  '))
    if options == 1:
        #number_quiz
    elif options == 2:
        #month_quiz
    elif options == 3:
        #daysoftheweekquiz
    elif options == 0:
        #exit
    else:
        print('Enter an integer')
        













random_number = random.randint(0, 9)
    


def number_questions():
    questions = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    question = questions[random_number]
    return question


def number_answers():
    answers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    answer = answers[random_number]
    print(answer)
    return answer


def cache():
    cache_list = ['tahi', 'tahi', 'tahi' 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']


number_questions()
number_answers()

