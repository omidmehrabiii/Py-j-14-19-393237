




height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal weight")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")