print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult ticket is $12.")
    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        print(f"Your final bill is ${bill + 3}")
    else:
        print(f"Your final bill is ${bill + 0}")

else:
    print("Sorry, you have to grow taller before you can ride.")