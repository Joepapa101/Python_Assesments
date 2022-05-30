import random
import time

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
        quit()


         
        
print('Ka pai to mahi e hoa!  Good job my friend!  You have completed the quiz.')
print(error_checker)