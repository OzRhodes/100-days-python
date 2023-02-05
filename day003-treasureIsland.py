print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your quest is to find the treasure. There are 2 slides in front of you") 

choice1 = input("Enter Left or Right: ").lower()
while choice1 not in ['left','right']:
	choice1 = input("Enter Left or Right: ").lower()	
if choice1 == "right":
	print("This slide led you to a spiky end...Game Over.")
else:
	print("Nice, you made it to the next level!")

	choice2 = input("You now need to get to Treasure Island, you can wait to board a ship or swim across the sea, pick one. Swim/Wait: ").lower()
  
	while choice2 not in ['wait','swim']:
		choice2 = input("Enter wait or swim: ").lower()	
	if choice2 == "swim":
		print("Unfortunately, you were eaten by piranha...Game Over.")
	else:
		print("Nice, you made it to the next level, you're pretty good at this!")
		print ("Welcome to the Island.")

		choice3 = input("Now that you've made it to Treasure Island, you can dig or search the cave. Type Cave or Dig: ").lower()
		while choice3 not in ['cave','dig']:
			choice3 = input("Enter Cave or Dig: ").lower()	
		if choice3 == "dig":
			print("You've found the treasure, you win!")
		else:
			print("You were eaten by a sasquatch... Game Over.")
