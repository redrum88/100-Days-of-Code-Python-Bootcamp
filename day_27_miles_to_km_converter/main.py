from tkinter import *


def button_clicked():
    print("I got clicked")
    user_input = int(input.get())
    user_input *= 1.60934
    result.config(text=round(user_input, 1))


window = Tk()
window.title("Mile to Km Calculator")
window.minsize(width=250, height=150)
window.config(padx=35, pady=25)

# Label
result = Label(text="I Am a Label", font=("Arial", 8, "bold"))
result.config(text=0)
# my_label.place(x=0, y=0)
result.grid(column=1, row=1)
# my_label.config(padx=50, pady=50)

# Label
label_1 = Label(text="I Am a Label", font=("Arial", 8, "bold"))
label_1.config(text="is equal to")
# my_label.place(x=0, y=0)
label_1.grid(column=0, row=1)
# my_label.config(padx=50, pady=50)
label_2 = Label(text="I Am a Label", font=("Arial", 8, "bold"))
label_2.config(text="Miles")
# my_label.place(x=0, y=0)
label_2.grid(column=2, row=0)

label_3 = Label(text="I Am a Label", font=("Arial", 8, "bold"))
label_3.config(text="Km")
# my_label.place(x=0, y=0)
label_3.grid(column=2, row=1)

# Button
button = Button(text="Calculate", font=("Arial", 8, "bold"), command=button_clicked)
button.grid(column=1, row=3)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()
