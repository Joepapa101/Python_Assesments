from ast import Expression
import random
import time
list_picker = 0



def useranswer1(current_question, current_answer):
    numbers10 = ['tahi', 'rua', 'toru', 'whā', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    answers10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    list_picker = random.randint(0, 9)
    current_question.var = (numbers10[list_picker])
    current_answer = (answers10[list_picker])
    print(current_question)
    return current_question, current_answer

current_question = current_question.var
current_answer = 

    
    

useranswer1()
print(f'What is {current_question} in English')
user = input('Whats this number?  Enter in english:  ')
if current_answer == user:
    print('Good job')
else:
    print(f"That's actually {current_answer}")
    time.sleep(2)
    enter = input('Press ENTER to continue')

useranswer1()
print(current_question)



