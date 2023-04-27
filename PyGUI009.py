# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:13:29 2023

@author: prati
"""
import pandas as pd
df = pd.read_csv("C:\\Pratibha\Code\\Python\\Python Exercise\\Automobile_data.csv")
print("Printing First Five Rows from the file")
print(df.head(5))
print("Printing Last Five Rows from the file")
print(df.tail(5))

