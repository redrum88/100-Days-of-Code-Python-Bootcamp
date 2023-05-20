# 🚨 Don't change the code below 👇
height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi = weight / (height * height)
bmi = round(weight / height ** 2)

categories = [
    (18.8, "underweight"),
    (25, "normal weight"),
    (30, "overweight"),
    (35, "obese"),
]

category = "clinically obese"  # Default

for i, label in categories:
    if bmi < i:
        category = label
        break

print(f"Your BMI is {bmi}, you are {category}.")
