import random
current_question = ''
current_answer = ''

numbers10 = ['kore','tahi', 'rua', 'toru', 'whā', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau', 'tekau mā tahi', 'tekau mā rua', 'tekau mā toru', 'tekau mā whā', 'tekau mā rima', 'tekau mā ono', 'tekau mā whitu', 'tekau mā waru', 'tekau mā iwa', 'rua tekau']
answers10 = ['zero' and 0, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninteen', 'twenty']
numbers20 = []
while current_answer != 'zero':
    list_picker = random.randint(0, 20)
    current_question = (numbers10[list_picker])
    current_answer = (answers10[list_picker])
    print(current_question)
    user = input(f'Whats {current_question}:  ')
    if current_answer == user:
        print('Good job') 
    else:
        print('Error 404 lol')