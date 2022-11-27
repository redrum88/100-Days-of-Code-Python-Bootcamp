import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generate():
    user_input = input("Enter name to show NATO phonetic alphabet: ").upper()
    try:
        user_words = [alphabet[letter] for letter in user_input]
        print(user_words)
        generate()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()


generate()
