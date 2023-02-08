# Use functions for inouts and outputs
# ask 'what the first number'
# ask 'what is the operator'
# ask 'what is the second number'
# present the answer
# usd a dictionary and multiple functions

def add(num1, num2):
		return num1 + num2
		
def subtract(num1, num2):
			return num1 - num2

def multiply(num1, num2):
			return num1 * num2

def divide(num1, num2):
		return num1 / num2

# create a dictionary of operators
operators = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

for operator in operators:
	print(operator) # print the keys

num1 = float(input("what's the first number? " ))

num2 = float(input("what's the second number? " ))


operation = input("what's the operator? " )

op_function = operators[operation] # return a string that is the name of the function to be called

result = op_function(num1, num2) # call the function

print(f"Result of {num1} {operation} {num2} is {result} ")
