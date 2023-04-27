# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:21:43 2023

@author: prati
"""

import pandas as pd
df = pd.read_csv("C:\\Pratibha\\TestFile\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
priceDf
print(priceDf)