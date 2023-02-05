# get inputs for height and weight and claculated the BMI
# BMI = weight in kg / height**2 in metres

height = float(input("please enter your height in meters: "))
weight = float(input("please enter your weight in kilogrammes: "))

bmi = weight / (height**2)

print (f"your BMI is {bmi:.2f}")
