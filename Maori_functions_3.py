import random



def number_quiz():
    counter = 3
    numbers = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    answers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    times_answered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    answer_generator = random.randint(0, 9)
    question = numbers(answer_generator)
    answer = answers(answer_generator)
    user = input(f'What is {question} in english:  ')
    if user == answer:
        print('Good Job')
        times_answered[answer_generator] += 1
        print(times_answered)
    else:
        print('sryy')
            



def days_of_the_week():
    days = ['Rāhina', 'Rātu', 'Rāapa', 'Rāpare', 'Rāmere', 'Rāhoroi', 'Rātapu']
    answers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

number_quiz()


