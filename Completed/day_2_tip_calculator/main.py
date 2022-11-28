print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
each = total_bill / people
result = round(each, 2)
result = "{:.2f}".format(each)
print(f"Each person should pay: ${result}")
