# -*- coding: utf-8 -*-
"""suniymaruza3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12_9iZAEw1n6Iq0xOn9mS18fKi0ast5D7
"""

import pandas as pd
import numpy as np

dff=pd.read_excel("/content/sample_data/Narxlar.xlsx",index_col=0)
dff

dff.loc['Osh']

bins=[0,10000,30000,100000]

population=dff.Narxi
population

values=["arzon","urtacha","qimmat"]
array=pd.cut(population,bins, labels=values)
array