import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hands = [rock, paper, scissors]

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choise >= 3:
    print("You typed an invalid number")
else:
    computer_choise = random.randint(0, 2)
    print(hands[user_choise])
    print("Computer chose:")
    print(hands[computer_choise])

    if user_choise >= 3 or user_choise < 0:
        print("You typed an invalid number, you lose!")

    elif user_choise == 0 and computer_choise == 2:
        #  print(hands[user_choise])
        #  print(f"Computer chose:")
        #  print(hands[computer_choise])
        print("You win!")
    elif computer_choise == 0 and user_choise == 2:
        #  print(hands[user_choise])
        #  print(f"Computer chose:")
        #  print(hands[computer_choise])
        print("You lose!")
    elif computer_choise > user_choise:
        #  print(hands[user_choise])
        #  print(f"Computer chose:")
        #  print(hands[computer_choise])
        print("You lose!")
    elif user_choise > computer_choise:
        #  print(hands[user_choise])
        #  print(f"Computer chose:")
        #  print(hands[computer_choise])
        print("You win!")
    elif computer_choise == user_choise:
        #  print(hands[user_choise])
        #  print(f"Computer chose:")
        #  print(hands[computer_choise])
        print("It's a draw!")

# Write your code below this line 👇
