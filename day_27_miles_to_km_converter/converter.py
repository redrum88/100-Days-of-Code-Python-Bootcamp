from tkinter import *

def miles_to_km():
    kilometers = float(miles_input.get())
    kilometers *= 1.60934
    result.config(text=round(kilometers, 2))

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)








window.mainloop()