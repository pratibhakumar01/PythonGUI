# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:09:00 2023

@author: prati
"""
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

num = int(input("Enter your number to check Palindrome: "))

revnum = reverse(num)

if num - revnum ==0:
    print(num," is a Palindrome number")
else:
    print(num," is not a Palindrome number")


#logic to reverse the number
