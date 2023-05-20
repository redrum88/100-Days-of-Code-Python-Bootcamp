# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year.")
else:
    print("Not a leap year.")

