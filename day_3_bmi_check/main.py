# 🚨 Don't change the code below 👇
height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = weight / (height * height)
bmi = round(weight / height ** 2)

if bmi < 18.8:
    print(f"Your bmi is {bmi}, you are underweight.")

elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")

elif bmi < 30:
    print(f"Your bmi is {bmi}, you are underweight.")

elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")

else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
