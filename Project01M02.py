# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:48:36 2023

@author: prati
"""
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font

# create root window
root = Tk()

# Set geometry(widthxheight)
root.geometry('800x500')
# adding a header label to the root window
Login_Page_Label = Label(root, text = "IOT Dashboard",font=("Arial",15))
Login_Page_Label.place(relx = 0.5,
                   rely = 0.025,
                   anchor = 'center')
Login_Page_Label.config(bg="red")



# Execute Tkinter
root.mainloop()