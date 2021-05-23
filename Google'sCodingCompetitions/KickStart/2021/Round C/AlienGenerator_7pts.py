
def gen_sol(G):
    n = 0
    for i in range(0, (3162277+1)//2 ):
        if G%(2*i+1)==0 and (i)<G:
            #n = n+1
            n = n+1
    return n

T = int(input())

for i in range(T):
    G = int(input())

    # La idea es hacer busqueda binaria sobre todos los núumeros menores a Z
    sol = gen_sol(G)

    print(f'Case #{i+1}:', sol)
