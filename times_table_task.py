from tkinter import *
import random as rand


class MultiplicationCalculator:
    def __init__(self, window):
        f1 = Frame(window)
        f2 = Frame(window)
        label1 = Label(f1, text="Number x Number =")
        entry1 = Entry(f1)
        button1 = Button(f2, text="Check Answer")
        button2 = Button(f2, text="Next")

        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        button1.grid(row=0, column=0, sticky=W)
        button2.grid(row=0, column=1, sticky=E)
        f1.grid(row=0, column=0)
        f2.grid(row=1, column=0)


root = Tk()
calculator = MultiplicationCalculator(root)
root.mainloop()
