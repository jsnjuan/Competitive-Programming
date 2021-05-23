# Consecutive primes

import numpy as np
from bisect import bisect_right

def primesfrom2to(n):
    # Fuente general: https://stackoverflow.com/a/2068548
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]

#ls_primos = primesfrom2to(10**9+1)
ls_primos = primesfrom2to(10**7+1)
#len_ls_primos = len(ls_primos)
consecutivos = {ls_primos[i]*ls_primos[i+1] for i in range(len(ls_primos)-1)}
consecutivos = sorted(consecutivos)

T = int(input())

for i in range(T):
    Z = int(input())

    # La idea es hacer busqueda binaria sobre todos los núumeros menores a Z
    sol = find_le(consecutivos, Z)

    print(f'Case #{i+1}:', sol)
