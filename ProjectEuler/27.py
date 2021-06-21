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

# Given quadratic form n*n  + a*n + n = n*(n+a) + b, we will have a composite
# number whenever n+a=b, so we can safely get an upperbound for primes generation
# considering at worst case that n=a=b=1,000

ls_primos = primesfrom2to(10**7+1)
print('So far we have generated primes from 2 to 10**7+1')

def gen_qf(a, b):
    def qf(n):
        return n*n + a*n + b
    return qf

def np_qf(a, b):
    qf = gen_qf(a=a,b=b)
    n = 0
    while qf(n) in ls_primos:
        n+=1
    return n

# Lets try formulaes with  quadratic forms from problem's description
print('test 41:', np_qf(a=1, b=41))
print('test n^2 - 79n + 1601:', np_qf(a=-79, b=1601))

# As we are starting at n=0, b should be prime, so we generate coeficient
# candidates, where b is prime
st_b = set()
for b in ls_primos:
    if b>1_000:
        break
    st_b.add(b)

print('We have generated "b" coeficient candidates. #:', len(st_b))

max_np = 0
a_max_np = None
b_max_np = None

for a in range(-1_000,1_000+1):
    for b in st_b:
         s = np_qf(a, b)
         if  s>=max_np:
             max_np = s
             a_max_np = a
             b_max_np = b

print(f'a ={a_max_np}, b={b_max_np}, # primes={max_np}')
print(f'Solution={a_max_np*b_max_np}')
