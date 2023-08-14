## Creating a calculator 

import tkinter 

root = tkinter.Tk()
root.title("clculator")

expression = ""

# Creating an add function 

def add(value):
    global expression
    expression += value
    label_result.config(text=expression)

def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
