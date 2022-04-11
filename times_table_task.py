from tkinter import *
import random


class Interface:
    def __init__(self, window):
        self.c = Calculator()
        self.question = Label(window, text="")
        self.question.grid(row=0, column=0)

        self.user_answer = Entry(window)
        self.user_answer.grid(row=0, column=1)

        check_button = Button(window, text="Check Answer", command=self.checker)
        check_button.grid(row=1, column=0)

        next_button = Button(window, text="Next", command=self.new_num)
        next_button.grid(row=1, column=1)

        self.response = Label(window, text="Please type in your answer")
        self.response.grid(row=0, column=2)

        self.new_num()

    def checker(self):
        if self.c.answer_func(self.user_answer.get()):
            self.response.configure(text="Correct!")
        else:
            self.response.configure(text="Incorrect!")

    def new_num(self):
        self.c.num_changer()
        self.question.configure(text=f"{self.c.number1} x {self.c.number2} =")


class Calculator:
    def __init__(self):
        self.number1 = random.randint(0, 10)
        self.number2 = random.randint(0, 10)

    def answer_func(self, answer):
        return answer == str(self.number1*self.number2)

    def num_changer(self):
        self.number1 = random.randint(0, 10)
        self.number2 = random.randint(0, 10)


root = Tk()
calculator = Interface(root)
root.mainloop()
