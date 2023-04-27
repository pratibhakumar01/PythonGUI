# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:28:27 2023

@author: prati
"""
print('Printing current and previous number sum in a range(10)')
count = 0
previous = 0
"""while (count < 10):
   print ("The current number ", count, "previous number ", previous , "Sum :", count + previous)
   previous = count
   count = count + 1
print(count)"""
count = 0
previous = 0
for count in range(0,10):
   print ("The current number ", count, "previous number ", previous , "Sum :", count + previous)
   previous = count
   count = count + 1  
