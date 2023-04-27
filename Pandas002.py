# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:01:41 2023

@author: prati
"""

import pandas as pd

df = pd.read_csv("C:\\Pratibha\\TestFile\\Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)

df.to_csv("C:\\Pratibha\\TestFile\\Automobile_data.csv")