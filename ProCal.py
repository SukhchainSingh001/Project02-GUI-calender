from tkinter import *
from tkcalendar import *

pr = Tk()
pr.title("Calender")
pr.geometry("350x300")


Cal = Calendar(pr, selectmode = "day", year = 2012, month = 3, day = 3)
Cal.pack(pady = 20)


def get_date():
    label.config(Text = Cal.get_date())


button = Button(pr, text = "Select the date", command= get_date)
button.pack(pady=20)

label = Label(pr, text="")
label.pack(pady=20)

pr.mainloop()



