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

ls_primos = primesfrom2to(1_000_000)

def is_prime(x):
    return x in ls_primos
    if x<2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x%i==0:
            return False
    return True

def l2r(p):
    while p:
        if not is_prime(p):
            return False
        p//=10
    return True

def r2l(p):
    while p:
        if not is_prime(p):
            return False
        p=int(str(p)[1:]) if str(p)[1:] else 0
    return True

cnt = 1
ls_sol = []
for p in ls_primos[4:]:
    if l2r(p) and r2l(p):
        print(cnt, ':', p)
        cnt += 1
        ls_sol.append(p)

print('Solution:', sum(ls_sol))
