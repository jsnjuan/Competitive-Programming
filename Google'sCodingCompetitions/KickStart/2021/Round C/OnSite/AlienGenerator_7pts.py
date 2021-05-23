
def gen_sol(G):
   # given n= days, k= initial gold bars, G= desired golden bars
   # we have that following equation must be satisfied:
   # n(  k + (n-1)/2 ) = G
   # Remember n and k are unknown. One insight we can note is the following:
   #  because k is an integer, n must be not only a divisor of G, but also it
   # should be an odd integer, in order to the equation be satisfied.
   # with this in hand, we can implement a naive solution in
   # wich n' is in [0, G/2] and is such that n = 2*n' + 1

    n = 0
    for i in range(0, (G+1)//2):
        if G%(2*i+1)==0 and G//(2*i+1)>0:
            n = n+1
    return n

T = int(input())

for i in range(T):
    G = int(input())

    # La idea es hacer busqueda binaria sobre todos los núumeros menores a Z
    sol = gen_sol(G)

    print(f'Case #{i+1}:', sol)
