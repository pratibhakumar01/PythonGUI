# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:25:29 2023

@author: prati
"""

def remove_chars(x,y):
    if len(x)<=y:
        print("Your String does not has enough character to remove")
    else:
        print(x[y:])
    
input_str = str(input("Enter the String: "))
input_rem = int(input("Enter the number of characters to be removed: "))
    
remove_chars(input_str, input_rem)
