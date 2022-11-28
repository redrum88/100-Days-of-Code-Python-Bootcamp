import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct.",
                                    prompt="What's another state's name?").title()

    # print(answer_state)

    # If answer_state is one of the states in all the states of 50 states csv
    # if they got it right:
    # create a turtle to write the name of the state

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

    # score = turtle.Turtle()
    # score.hideturtle()
    # score.penup()
    # score.goto(0, 250)
    # score.write(f"You guessed right {len(guessed_states)} states of 50.")
    # print(f" {len(guessed_states)}/50")
# screen.exitonclick()
