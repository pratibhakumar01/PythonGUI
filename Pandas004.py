# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:27:51 2023

@author: prati
"""

import pandas as pd
df = pd.read_csv("C:\\Pratibha\\TestFile\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf
print(toyotaDf)
