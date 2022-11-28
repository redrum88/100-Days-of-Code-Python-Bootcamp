# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# letter true
name1_lower = str.lower((name1))
name2_lower = str.lower((name2))
name_lower = name1_lower + name2_lower
# print(f"Two names together {name_lower}")
letter1 = name_lower.count("t")
letter2 = name_lower.count("r")
letter3 = name_lower.count("u")
letter4 = name_lower.count("e")
word_true = letter1 + letter2 + letter3 + letter4
# print(letter1 + letter2 + letter3 + letter4)
letter5 = name_lower.count("l")
letter6 = name_lower.count("o")
letter7 = name_lower.count("v")
letter8 = name_lower.count("e")
# print(letter5 + letter6 + letter7 + letter8)
word_love = letter5 + letter6 + letter7 + letter8
love_count = f"{str(word_true)}{str(word_love)}"
love_count = int(love_count)
# print(love_count)
if love_count < 10 or love_count > 90:
    print(f"Your score is {love_count}, you go together like coke and mentos.")
elif love_count >= 40 and love_count <= 50:
    print(f"Your score is {love_count}, you are alright together.")
else:
    print(f"Your score is {love_count}.")
