# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:28:05 2023

@author: prati
"""

# Import Module
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
                   rely = 0.1,
                   anchor = 'center')
Login_Page_Label.config(bg="limegreen")

# adding a header label to the root window
Login_Page_Header= Label(root, text = "Welcome Board",font=("Arial",10))
Login_Page_Header.place(relx = 0.25,
                   rely = 0.2,
                   anchor = 'ne')
Login_Page_Header.config(bg="darkorange")
#adding a left image to the login page
left_image = ImageTk.PhotoImage(file='C:\Pratibha\Code\Python\Python Exercise\Pictures\left.PNG')
Login_Page_Left = Label(root, image=left_image)
Login_Page_Left.place(relx = 0.4,
                   rely = 0.3,
                   anchor = 'ne')
#adding a right image to the login page
right_image_o= Image.open("C:\Pratibha\Code\Python\Python Exercise\Pictures/right.PNG")
right_image_r = right_image_o.resize((300,200))
right_image = ImageTk.PhotoImage(right_image_r)
Login_Page_Right= Label(root, image=right_image)
Login_Page_Right.place(relx=.56,rely=.4,anchor='nw')

#Function to Request username and password when clicked on login
def clicked():
    e1=Entry()
    e1.place(x=350,y=190,width=75,height=20)
    e1.insert(2,'Username')
    e2=Entry()
    e2.place(x=350,y=250,width=75,height=20)
    e2.insert(0,'Password')
    b2 = Button(root,text = "Enter",bg="orange", command=display_device)
    b2.place(x=350,y=300)    

def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

def display_device():
    Frame1 = Frame()
    Frame1.place(x=0,y=0,width=800,height=500)
    make_label(Frame1, 310, 15, 30, 180, text='IOT DASHBOARD', font=("Arial",10),background='red')
    make_label(Frame1, 75, 60, 40, 240, text='WELCOME BOARD IOT BOARD', background='orange')
    make_label(Frame1, 450, 60, 40, 280, text='DISPLAY DEVICE NAME TO CONNECT', background='green')
    Login_Button = Button(Frame1, text = "DEVICE1", bg="pink",font="Arial")
    Login_Button['font']= font.Font(size=12)
    Login_Button.place(relx = 0.7, rely = 0.35, anchor = 'center')
    Login_Button = Button(Frame1, text = "DEVICE2", bg="yellow",font="Arial")
    Login_Button['font']= font.Font(size=12)
    Login_Button.place(relx = 0.7, rely = 0.45, anchor = 'center')
    Login_Button = Button(Frame1, text = "DEVICE3", bg="pink",font="Arial")
    Login_Button.place(relx = 0.7, rely = 0.55, anchor = 'center')
    Login_Button['font']= font.Font(size=12)
    Login_Button = Button(Frame1, text = "DEVICE4", bg="purple",font="Arial")
    Login_Button['font']= font.Font(size=12)
    Login_Button.place(relx = 0.7, rely = 0.65, anchor = 'center')
    device_left_image_o= Image.open("C:\Pratibha\Code\Python\Python Exercise\Pictures/IOTpage2.PNG")
    device_left_image_r = device_left_image_o.resize((100,100))
    device_left_image = ImageTk.PhotoImage(device_left_image_r)
    make_label(Frame1,25,100,100,100,image=device_left_image)
   # Device_Page_left= Label(Frame1, image=device_left_image)
   # Device_Page_left.place(relx=.05,rely=.3,anchor='nw')

#adding the login button
Login_Button = Button(root, text = "Login Details", bg="Gold", font="Arial", command=clicked)
Login_Button['font']= font.Font(size=12)
Login_Button.place(relx = 0.5, rely = 0.3, anchor = 'center')

# Execute Tkinter
root.mainloop()
