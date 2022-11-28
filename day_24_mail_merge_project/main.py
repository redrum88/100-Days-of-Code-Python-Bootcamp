PLACEHOLDER = "[name]"

# File with names to use generate letters
with open("./input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)


# Take template letter and replace name and create new letter for each name
with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, f"{stripped_name}")
        with open(f"./output/letter_to_{stripped_name}", mode="w") as output_file:
            output_file.write(new_letter)
