from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
PADDING = 20
HEIGHT = 250
WIDTH = 300
SCORE = 0


class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # MAIN WINDOW
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)

        # ALL IMAGES
        self.red_picture = PhotoImage(file="images/false.png")
        self.green_picture = PhotoImage(file="images/true.png")

        # SCORE LABEL
        self.score_label = Label(text=f"Score: {SCORE}", bg=THEME_COLOR, font=FONT)

        # QUESTION CANVAS
        self.canvas = Canvas(width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.config()
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR,
                                                     font=FONT)

        # BUTTONS
        self.red_button = Button(image=self.red_picture, highlightthickness=0, command=self.press_red)
        self.green_button = Button(image=self.green_picture, highlightthickness=0, command=self.press_green)

        # GRID ELEMENTS ON SCREEN
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.red_button.grid(row=2, column=1)
        self.green_button.grid(row=2, column=0)
        self.get_next_question()
        # MAIN SCREEN LOOP
        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You Have Reach End of The Quiz.")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def press_green(self):
        self.feedback(self.quiz.check_answer("True"))

    def press_red(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000, self.get_next_question)
