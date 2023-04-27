# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:13:55 2023

@author: prati
"""

import pandas as pd
df = pd.read_csv("C:\\Pratibha\\TestFile\\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
print(df)