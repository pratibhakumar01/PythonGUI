# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 09:05:23 2023

@author: prati
"""

# Import Module
from tkinter import *

# create root window
root = Tk()
root.title("Simple Calculator")
frame= Frame(root, bg="skyblue", padx=10)
frame.pack()
e = Entry(frame, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_press(number):
    e.insert(END, number)

def clear():
    e.delete(0,END)

def equal():
    y=str(eval(e.get()))
    e.delete(0,END)
    e.insert(0,y)
#Define Buttons

button_1 = Button(frame, text="1", padx=40, pady=20, command=lambda: button_press(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command=lambda: button_press(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command=lambda: button_press(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command=lambda: button_press(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command=lambda: button_press(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command=lambda: button_press(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command=lambda: button_press(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command=lambda: button_press(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command=lambda: button_press(9))
button_0 = Button(frame, text="0", padx=40, pady=20, command=lambda: button_press(0))
button_add = Button(frame, text="+", padx=40, pady=20, command=lambda: button_press('+'))
button_sub = Button(frame, text="-", padx=40, pady=20, command=lambda: button_press('-'))
button_mul = Button(frame, text="*", padx=40, pady=20, command=lambda: button_press('*'))
button_div = Button(frame, text="/", padx=40, pady=20, command=lambda: button_press('/'))
button_equal = Button(frame, text="=", padx=40, pady=20, command=lambda: equal())
button_clear = Button(frame, text="clear", padx=80, pady=20, command=lambda: clear())
    
# put the buttons on the screen 

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0, columnspan=3)

button_add.grid(row=5,column=0)
button_sub.grid(row=5,column=1)
button_mul.grid(row=5,column=2)

button_div.grid(row=6, column=0)
button_clear.grid(row=6, column=1, columnspan=2)

button_equal.grid(row=7, column=1)

# Execute Tkinter
root.mainloop()