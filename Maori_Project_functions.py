import random
def question_answer():
    questions = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
    answers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    final_answer_calculator = random.randint(0, 9)
    question = questions[final_answer_calculator]
    answer = answers[final_answer_calculator]
    return question, answer

question = question_answer()
answer = question_answer()



def main():
    print

#main routine
print(question_answer)
main()

