# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:29:12 2023

@author: prati
"""

# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Pratibha's World")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
item.add_command(label='Open')
item.add_command(label='Save')
item.add_command(label='Close')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when
# button is clicked
def clicked():

	res = "You wrote" + txt.get()
	lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
			fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=1, row=5)

# Execute Tkinter
root.mainloop()
