# -*- coding: utf-8 -*-
"""
Created on Sat May 29 01:30:52 2021

@author: jaime
"""

import pandas as pd
# Busquemos un patrón de los dígitos de las potencias de 2

ls_tot = []
for i in range(1, 1001):
    n = 2 ** i
    n_str = str(n)
    ls_tot.append(list(n_str[::-1]) )

df = pd.DataFrame.from_records(ls_tot)

df.iloc[-1,:].map(int).sum()