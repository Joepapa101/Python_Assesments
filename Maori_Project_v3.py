import random


counter = 9
numbers = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
answers_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while counter != 0:
    answer_generator = random.randint(0, counter)
    question = numbers[answer_generator]
    answer = answers_words[answer_generator]
    user = input(f'What is {question} in english:  ')
    if user == answer:
        print('Correct')
        times_answered[answer_generator] += 1
        print(times_answered)
        if times_answered[answer_generator] == 3:
            numbers.remove(question)
            answers_words.remove(answer)
            times_answered.remove(3)
            counter -= 1
            print(numbers)
            print(answers_words)
            print(times_answered)
            print('')
    elif user != answer and user == answers_words:
        print('Incorrect')
    else:
        print('Please enter the word for the number')