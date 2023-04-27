# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:01:42 2023

@author: prati
"""

def compare(list):
    x=list[0]
    y=list[-1]
    if x==y:
        print("True")
    else:
        print("False")
number_x=[10,20,30,40,50,30]
compare(number_x)