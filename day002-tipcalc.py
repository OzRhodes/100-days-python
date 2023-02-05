# user enters a total bill
# user enters number of people splitting the bill
# user enters the percentage
# result is the amount to be paid by each person including tip

total_bill = float(input("Enter the total bill amount : $")) # convert string to float
payers = int(input("Enter the number of people that will be paying : ")) # convert string to int people
tip_percent = int(input("Enter the percentage tip to be added - 10, 12 or 15%"))# convert string to float

while tip_percent not in [10,12,15]:
	tip_percent = float(input("Enter the percentage tip to be added - 10, 12 or 15%"))

calc = total_bill * (1+(tip_percent/100))/payers

print(f"The total each person will pay is $ {calc:.2f}")
