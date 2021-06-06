# -*- coding: utf-8 -*-
"""
Created on Sat May 29 01:49:23 2021

@author: jaime
"""

from math import sqrt

def abundant(n):
    st_divs = set()
    for d in range(1,  int(sqrt(n)) + 1 ):
        div1 = d
        div2 = n//d
        if n%div1==0 and div1!=n:
           st_divs.add(div1)
        if n%div2==0 and div2!=n:
           st_divs.add(div2)
    return n<sum(st_divs)
    

n = 28123
st_abundant_numbers = set()

for i in range(12,n+1): # n+1):
    if abundant(i):
        st_abundant_numbers.add(i)
        print(i)
    
# Hasta aquí ya tenemos la lista de números abundantes

def sum_abundants(i):
    for j in range(1, i):
        if j in st_abundant_numbers and i-j in st_abundant_numbers:
            return True
    return False

sol = 0
for i in range(1, n+1):
    if not sum_abundants(i):
        print(f'{i} is the sum of two abundant')
        sol+=i
        
        
print(sol)