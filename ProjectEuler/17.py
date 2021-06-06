# -*- coding: utf-8 -*-
"""
Created on Sat May 29 02:07:46 2021

@author: jaime
"""

dc1 = {1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
       8:'eight', 9:'nine',10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 
       14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 
       18:'eighteen', 19:'nineteen'}

dc2 = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
       70:'seventy', 80:'eighty', 90:'ninety'}

def n_to_words(n):
    if n < 20:
        return dc1[n]
    if  20<=n<=99:
        if n%10:
            return dc2[n - n%10] + ' ' + dc1[n%10]        
        else:
            return dc2[n]
    if 100<=n<=999:
        if n%100:
            return dc1[n//100] + ' hundred and ' + n_to_words(n%100)
        else:
            return dc1[n//100] + ' hundred'
    if n==1_000:
        return 'one thousand'
    
letters = 0
for i in range(1, 1_000 + 1):
    cad = n_to_words(i)
    letters += len(cad.replace(' ', ''))
    
print(letters)
