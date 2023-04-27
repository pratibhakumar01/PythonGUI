# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:51:37 2023

@author: prati
"""

# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')

#adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# Execute Tkinter
root.mainloop()
