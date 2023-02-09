

# set difficulty
# choose random number between 1-100
# get a guess
# check guess is too high or too low or correct
# track the number of goes

import random

def get_number():
	number = random.randint(1,100)
	return number
	
# input details
print("Welcome to the guessing game!")
diff = input("Choose a difficulty. Type 'easy' or 'hard' :")
while diff.lower() !='easy' and diff.lower() != 'hard':
	diff = input("Choose a difficulty. Type 'easy' or 'hard' :")

# set guesses
if diff == 'easy':
	guesses = 10
else:
	guesses = 5

#get the number
number = get_number()
print(number)# testing
guess = 0
while guess != number:
	guess = int(input("Make a guess : "))
	guesses -= 1
	if guess > number:
		print("too high!")
	elif guess < number:
		print("too low")
	else:
		print("Correct")
	if guesses == 0:
		print("out of guesses..you loose")
		break




