# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:40:18 2023

@author: prati
"""

num = int(input("Enter the number for formatting: "))
str1=""
temp=0
while num > 0:
    temp=num%10
    str1=str1+str(temp)+" "
    num=num//10
print(str1)