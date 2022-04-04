from tkinter import *
import random as rand


class MultiplicationCalculator:
    def __init__(self, window):
        f1 = Frame(window)
        f2 = Frame(window)
        number1 = rand.randint(0, 15)
        number2 = rand.randint(0, 15)
        self.answer = number1*number2
        label1 = Label(f1, text=f"{number1} x {number2} = ")
        self.entry1 = Entry(f1)
        button1 = Button(f2, text="Check Answer")
        button2 = Button(f2, text="Next")
        self.response = Label(f1, text="Please type in your answer")

        label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        f1.grid(row=0, column=0)
        f2.grid(row=1, column=0)

    def checker(self):
        if self.entry1.get() == self.answer:
            self.response.configure(text="Correct!")
        else:
            self.response.configure(text="Incorrect!")


root = Tk()
calculator = MultiplicationCalculator(root)
root.mainloop()
