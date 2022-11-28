# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters_total = len(letters)
numbers_total = len(numbers)
symbols_total = len(symbols)
print(f"Total letters: {letters_total} Total numbers: {numbers_total} Total symbols: {symbols_total}")
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(numbers)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
###############################################
# Start of random letters generator
# letter_pass = "" #
# def random_letter(nr_letters, letters):
#   return ''.join(random.choice(letters) for x in #range(nr_letters))
# letter_pass = random_letter(nr_letters, letters)
# End of random letters geenrator
###############################################
# print(f"This is random letters: {letter_pass}")
###############################################
# Start random symbol generator
# symbol_pass = ""
# def random_symbol(nr_symbols, symbols):
#   return ''.join(random.choice(symbols) for x in #range(nr_symbols))
# symbol_pass = random_symbol(nr_symbols, symbols)
# End of symbols generator
###############################################
# print(f"This is random symbols: {symbol_pass}")

###############################################
# Start of random number generator
# number_pass = ""
# def random_number(nr_numbers, numbers):
#  return ''.join(random.choice(numbers) for x in #range(nr_numbers))
# number_pass = random_number(nr_numbers, numbers)
# This is end of number generator
# print(f"This is random numbers: {number_pass}")
# password = letter_pass + symbol_pass + number_pass
# password_random = random.shuffle(password)
print(password)
# Convert string password to list
char_list = list(password)
random.shuffle(char_list)
random_password = ''.join(char_list)
print(random_password)
