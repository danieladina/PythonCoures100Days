from tkinter import *


def miles_to_km():
    miles=float(miles_input.get())
    answer=miles*1.609
    km_result.config(text=f"{answer}")

window = Tk()
window.title("miles to km converter")
window.config(padx=20, pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1, row=0)


miles_labal= Label(text="Miles")
miles_labal.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calc_button=Button(text="culculater",comman=miles_to_km)
calc_button.grid(column=2, row=1)











window.mainloop()
