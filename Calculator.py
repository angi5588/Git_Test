## simple calculator ##

from tkinter import *
import math

class Calculator:
    def __init__(self):
        window = Tk()
        window.title("Calculator")

        self.display = StringVar()
        Entry(window, textvariable = self.display, justify = RIGHT).grid(row = 1, column = 1, columnspan = 4, sticky = W+E)

        Button(window, text = "7", command = lambda: self.processDigit(7)).grid(row = 2, column = 1, sticky = W+E)
        Button(window, text = "8", command = lambda: self.processDigit(8)).grid(row = 2, column = 2, sticky = W+E)
        Button(window, text = "9", command = lambda: self.processDigit(9)).grid(row = 2, column = 3, sticky = W+E)
        Button(window, text = "+", command = lambda: self.processOperator("+")).grid(row = 2, column = 4, sticky = W+E)

        Button(window, text = "4", command = lambda: self.processDigit(4)).grid(row = 3, column = 1, sticky = W+E)
        Button(window, text = "5", command = lambda: self.processDigit(5)).grid(row = 3, column = 2, sticky = W+E)
        Button(window, text = "6", command = lambda: self.processDigit(6)).grid(row = 3, column = 3, sticky = W+E)
        Button(window, text = "-", command = lambda: self.processOperator("-")).grid(row = 3, column = 4, sticky = W+E)

        Button(window, text = "1", command = lambda: self.processDigit(1)).grid(row = 4, column = 1, sticky = W+E)
        Button(window, text = "2", command = lambda: self.processDigit(2)).grid(row = 4, column = 2, sticky = W+E)
        Button(window, text = "3", command = lambda: self.processDigit(3)).grid(row = 4, column = 3, sticky = W+E)
        Button(window, text = "*", command = lambda: self.processOperator("*")).grid(row = 4, column = 4, sticky = W+E)

        Button(window, text = "0", command = lambda: self.processDigit(0)).grid(row = 5, column = 1, sticky = W+E)
        Button(window, text = ".", command = lambda: self.processOperator(".")).grid(row = 5, column = 2, sticky = W+E)
        Button(window, text = "=", command = self.processEqual).grid(row = 5, column = 3, sticky = W+E)
        Button(window, text = "/", command = lambda: self.processOperator("/")).grid(row = 5, column = 4, sticky = W+E)

        window.mainloop() 

    def processDigit(self, digit):
        self.display.set(self.display.get() + str(digit))

    def processOperator(self, operator):
        if operator in "+-*/":
            self.display.set(self.display.get() + " " + operator + " ")
        else:
            self.display.set(self.display.get() + operator)

    def processEqual(self):
        try:
            self.display.set(eval(self.display.get()))
        except:
            self.display.set("Error")

Calculator()