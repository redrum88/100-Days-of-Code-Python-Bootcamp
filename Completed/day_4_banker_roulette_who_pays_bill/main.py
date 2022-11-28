import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

pay = random.choice(names)
print(f"Person who pays: {pay}")