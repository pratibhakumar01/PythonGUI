# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:18:39 2023

@author: prati
"""

def calculate(x,y):
    if x*y <= 1000:
        return x*y 
    else:
        return x+y

var1=int(input("Enter the first number"))
var2=int(input("Enter the second number"))
print("The calculation function of ", var1, "and ", var2, "returns ", calculate(var1,var2))


