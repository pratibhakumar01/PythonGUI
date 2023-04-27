# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:02:11 2023

@author: prati
"""

import pandas as pd
df = pd.read_csv("C:\\Pratibha\Code\\Python\\Python Exercise\\Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)

df.to_csv("C:\\Pratibha\Code\\Python\\Python Exercise\\Automobile_data.csv")