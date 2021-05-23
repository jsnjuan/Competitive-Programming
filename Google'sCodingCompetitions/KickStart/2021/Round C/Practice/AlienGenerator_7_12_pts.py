
from  math import sqrt

def gen_sol(G):
   # given n= days, k= initial gold bars, G= desired golden bars
   # we have that following equation must be satisfied:
   # n(  k + (n-1)/2 ) = G
   # Remember n and k are unknown.
   # First thing to notice is that n must divide G.
   # One insight we can note is the following:
   #  because k is an integer, n must be not only a divisor of G, but also it
   # should be an odd integer, in order to the equation be satisfied.
   # with this in hand, we can implement a naive solution in
   # wich n' is in [0, G/2] and is such that n = 2*n' + 1
   # This first idea is enough to pass Test Set 1

   # Second insight: actually, all divisors from a number can be obtained
   # iterating up to sqrt(G), so we can make this optimization to the code
    n = 0
    sqrt_G =int(sqrt(G))
    for i in range(1, sqrt_G+1):
        d1 = i
        d2 = G//d1
        if d1%2 and G%d1==0 and G//d1>0:
            n = n+1
        if d2>0 and d2%2 and G%d2==0 and G//d2>0 and d2!=d1:
            n = n+1

    return n

T = int(input())

for i in range(T):
    G = int(input())

    # La idea es hacer busqueda binaria sobre todos los núumeros menores a Z
    sol = gen_sol(G)

    print(f'Case #{i+1}:', sol)
