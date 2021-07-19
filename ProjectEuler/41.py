import numpy as np

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

def is_pand(p):
    cad_p = str(p)
    n = len(cad_p)
    for i in range(1, n + 1):
        if cad_p.count(str(i))!=1:
            return False
    return True

ls_primos = primesfrom2to(1_000_000_000)

largest_n_pand = 0
n = 0
for p in ls_primos:
    if is_pand(p) and p>largest_n_pand:
        largest_n_pand = p
        n = len(str(p))
        # print(f'Actualización: n = {n}, pandigital = {p}')

print(f'The largest {n}-pandigital prime is {largest_n_pand}')
