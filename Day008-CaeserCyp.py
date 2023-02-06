# user enters a encode or decode
# user enters a word
# user enters a shift
# output is a decoded or encoded
# we'll be using functions
# Ive chosen to use chr and ord
# lower case only so ords 61->122

def decode(msg,shft):
	output = []
	for letter in msg:
		ltr = ord(letter)
		ltr += shft
		if ltr > 122:
			ltr -=61
		output.append(chr(ltr))
	return output
				
	
def encode(msg,shft):
	output = []
	for letter in msg:
		ltr = ord(letter)
		ltr -= shft
		if ltr > 122:
			ltr -=61
		output.append(chr(ltr))	
	return output
			
	
	
def toString(msg):
	output = ''.join([str(item) for item in msg])
	return output
	
	
action = input("Enter encode or decode : ")
msg = input("Enter your message : ")
shft = int(input("Enter the shift : "))
	
if action == 'encode':
	print(toString(encode(msg,shft)))
		
if action == 'decode':
	print(toString(decode(msg,shft)))
	
	

