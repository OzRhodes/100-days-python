# Use functions for inouts and outputs
# ask 'what the first number'
# ask 'what is the operator'
# ask 'what is the second number'
# present the answer

def calc(num1, num2, op):
	if op == '+':
		return num1 + num2
	if op == '-':
		return num1 - num2
	if op == '/':
		return num1 / num2
	if op == '*':
		return num1 * num2

num1 = float(input("what's the first number? " ))

op = input("what's the operator? " )

num2 = float(input("what's the second number? " ))

print(f"result is {calc(num1, num2, op)}")




