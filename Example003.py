# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:31:53 2023

@author: prati
"""

python = str(input("Enter your string: "))

for i in range(len(python)):
    if i%2==0:
        print(python[i])
        
for i in range(len(python)):
    if i%2==1:
        print(python[i])