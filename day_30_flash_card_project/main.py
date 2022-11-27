# Import
from tkinter import *
import random
import pandas as pd

# DATA import CSV with pandas
try:
    new_data = pd.read_csv("data/need_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/spanish_words_1000.csv")
    all_words = data.to_dict(orient="records")
else:
    all_words = new_data.to_dict(orient="records")

# Globals
current = {}
current_number = len(all_words)
BACKGROUND_COLOR = "#B1DDC6"


# Function to give new card. After 3 sec change card to different color and text.
def give_card():
    global current, timer
    screen.after_cancel(timer)
    current = random.choice(all_words)
    card.itemconfig(title, text="Spanish", fill="black")
    card.itemconfig(word, text=current["Spanish"], fill="black")
    card.itemconfig(background, image=card_front_img)
    timer = screen.after(3000, func=flip_card)


# Function to change to new word.
def flip_card():
    card.itemconfig(title, text="English", fill="white")
    card.itemconfig(word, text=current["English"], fill="white")
    card.itemconfig(background, image=card_back_img)


def remove_card():
    global current_number
    all_words.remove(current)
    give_card()
    new_data = pd.DataFrame(all_words)
    new_data.to_csv("data/need_to_learn.csv", index=False)
    current_number = len(new_data)
    counter.config(text=f"Words remaining to learn: {current_number}")


# Tk Screen
screen = Tk()
screen.title("Flashy Spanish")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Timer to flip card
timer = screen.after(3000, func=flip_card)

# All Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Center Image "card".
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background = card.create_image(400, 263, image=card_front_img)
title = card.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=give_card)
right_button = Button(image=right_img, highlightthickness=0, command=remove_card)

# Counter Label
counter = Label(text=f"Words remaining to learn: {current_number}", bg=BACKGROUND_COLOR)

# Grid settings
card.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
counter.grid(row=2, column=0, columnspan=2)

# BOTTOM - Screen Main Loop
give_card()
screen.mainloop()
