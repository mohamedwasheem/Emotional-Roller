# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:06:38 2023

@author: User
"""

import pandas as pd
df = pd.read_csv("Reviews.csv")
cols = df.columns

empty_list = []
rest_df = pd.DataFrame({
    cols[0]:empty_list,
    cols[1]:empty_list,
    })

rest_df.to_csv("Reviews.csv",index=False)