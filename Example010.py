# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:04:34 2023

@author: prati
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3=[]

for num in list1:
    if num%2==1:
        list3.append(num)

for num2 in list2:
    if num2%2==0:
        list3.append(num2)
print(list3)