# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:16:14 2023

@author: prati
"""

import pandas as pd
df = pd.read_csv("C:\\Pratibha\\TestFile\\Automobile_data.csv")
df['company'].value_counts()
print(df)