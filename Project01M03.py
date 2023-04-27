# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:15:44 2023

@author: prati
"""

from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font
root = Tk()
root.geometry('800x500')

def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

make_label(root, 310, 15, 30, 180, text='IOT DASHBOARD', font=("Arial",10),background='red')
make_label(root, 75, 60, 40, 240, text='WELCOME BOARD IOT BOARD', background='orange')
make_label(root, 450, 60, 40, 280, text='DISPLAY DEVICE NAME TO CONNECT', background='green')
Login_Button = Button(root, text = "DEVICE1", bg="pink",font="Arial")
Login_Button['font']= font.Font(size=12)
Login_Button.place(relx = 0.7, rely = 0.35, anchor = 'center')
Login_Button = Button(root, text = "DEVICE2", bg="yellow",font="Arial")
Login_Button['font']= font.Font(size=12)
Login_Button.place(relx = 0.7, rely = 0.45, anchor = 'center')
Login_Button = Button(root, text = "DEVICE3", bg="pink",font="Arial")
Login_Button.place(relx = 0.7, rely = 0.55, anchor = 'center')
Login_Button['font']= font.Font(size=12)
Login_Button = Button(root, text = "DEVICE4", bg="purple",font="Arial")
Login_Button['font']= font.Font(size=12)
Login_Button.place(relx = 0.7, rely = 0.65, anchor = 'center')




#adding a left image to the login page
#left_image = PhotoImage(file='C:\Pratibha\Code\Python\Python Exercise\Pictures\IOTpage2.PNG')
#Login_Page_Left = Label(root, image=left_image)
#Login_Page_Left.place(relx = 0.7,
                  # rely = 0.3,
                  # anchor = 'ne')
                  
#adding a left image to the login page
left_image_o= Image.open("C:\Pratibha\Code\Python\Python Exercise\Pictures/IOTpage2.PNG")
left_image_r = left_image_o.resize((400,200))
left_image = ImageTk.PhotoImage(left_image_r)
Login_Page_left= Label(root, image=left_image)
Login_Page_left.place(relx=.05,rely=.3,anchor='nw')

root.mainloop()

