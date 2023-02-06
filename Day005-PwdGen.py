# requests the number of letters
# requests the number of symbols
# requests the number of numbers
# creates a new password

import random

letters = int(input("How many letters in the password?  "))
numbers = int(input("How many numbers in the password?  "))
symbols = int(input("How many symbols in the password?  "))

letter_lst =['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','L','K','J','H','G','F','D','S','A','Z','X','C','V','B','N','M']
number_lst =['1','2','3','4','5','6','7','8','9','0']
symbol_lst=['!','#','$','%','&','(',')','*','+']

# build a list of random letters, symbols and numbers
password_lst =[]
for letter in range(0,letters):
	password_lst.append(random.choice(letter_lst))
	
for number in range(0,numbers):
	password_lst.append(random.choice(number_lst))
	
for symbol in range(0,symbols):
	password_lst.append(random.choice(symbol_lst))


# random.shuffle
random.shuffle(password_lst)

# passsword_lst as string via comprehension

password = ''.join([str(item) for item in password_lst])


print(password)

