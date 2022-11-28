print('''
                       ;\
                      _' \_
                    ,' '  '`.
                   ;,)       \
                  /          :
                  (_         :
                   `--.       \
                      /        `.
                     ;           `.
                    /              `.
                   :                 `.
                   :                   \
                    \\                  \
                     ::                 :
                     || |               |
                     || |`._            ;
       Y            _;; ; __`._,       (________
   (t^##_          ((__/(_____(______,'______(___) SSt
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
answer1 = input(f'You\'re at a crossroad. Where do you want to go? Type "left" or "right" \n')
answer1 = answer1.lower()
if answer1 == "left":
    answer2 = input(
        f'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across \n')
    answer2 = answer2.lower()
    if answer2 == "wait":
        answer3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        answer3 = answer3.lower()
        if answer3 == "red":
            print('It\'s a room full of fire. Game Over.\n')
        elif answer3 == "blue":
            print("You enter a room of beasts. Game Over.\n")
        elif answer3 == "yellow":
            print("You found the treasure! You Win!\n")
        elif answer3 != "red" and answer3 != "blue" and answer3 != "yellow":
            print(f'You chose a door that doesn\'t exist. Game Over.\n')
    #  print("You fell into a hole. Game Over."''
    else:
        print("You get attacked by an angry trout. Game Over.\n")

else:
    print("You fell into a hole. Game Over.\n")
