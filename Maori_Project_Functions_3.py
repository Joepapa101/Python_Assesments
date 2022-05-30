import random

def questions_and_answers():
    questions = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    answers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    question = random(questions)
    answer = answers.index(question)
    return question

questions_and_answers()
print(f'This is the {questions_and_answers}')