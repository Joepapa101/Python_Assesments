import random

#list with all of the questions and answers   
numbers10 = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau']
answers10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
#a randomly generated number using an integer to pick a number from the list, the integer also picks the answer
list_picker = random.randint(0, 9)
#prints the randomly picked number for the user
print(numbers10[list_picker])
#the user inputs what they think the number is
user = input('Whats this number?  Enter in english')
#the program decides whether the number is right or wrong
if answers10 == user:
    print('Good job')
else:
    print('Sorry try again')

 
