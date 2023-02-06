# ask 0-Rock 1 paper 2 scissors

# you play the computer

# Adding ascii art could improve the feel but doesn't improve the lesson

import random

guess = input("Enter 0 for Rock, 1 for Paper or 2 for Scissors ")

while guess not in ["0","1","2"]:
	guess = input("Enter 0 for Rock, 1 for Paper or 2 for Scissors ")

guess = int(guess)

computer_guess = random.choice([1,2,3])

# could use random.randint(0,2)

if guess == computer_guess:
	print("Draw!")
elif guess ==1 and  computer_guess ==0:
	
	print(f"Player chose {guess} and computer chose {computer_guess}")
	print("Paper wraps rock")
	print ("Player wins")
elif guess ==2 and computer_guess == 1:
	
	print(f"Player chose {guess} and computer chose {computer_guess}")
	print("Scissors cut paper")
	print ("Player wins")
	
elif guess ==0 and computer_guess == 3:
	
	print(f"Player chose {guess} and computer chose {computer_guess}")
	print("Rock blunts scissors")
	print ("Player wins")

elif computer_guess ==1 and  guess ==0:
	
	print(f"Player chose {guess} and computer chose {computer_guess}")
	print("Paper wraps rock")
	print ("Computer wins")
elif computer_guess ==2 and guess == 1:
	
	print(f"Player chose {guess} and computer chose {computer_guess}")
	print("Scissors cut paper")
	print ("Computer wins")
	
elif computer_guess ==0 and guess == 3:
	print(f"Player chose {guess} and computer chose {computer_guess}")
	print("Rock blunts scissors")
	print ("Computer wins")
