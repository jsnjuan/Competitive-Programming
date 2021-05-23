T = int(input())

def gen_esc1(ls_int, K):
    ls_max = []
    for a,b in ls_int:
        if a==0:
            ls_max.append(b-1)
        elif b == (K+1):
            ls_max.append(K-a)
        else:
            ls_max.append(b-a-1)

    ls_max = sorted(ls_max)

    if not ls_max:
        return 0.

    else:
        return ls_max[-1]/K

def gen_esc2(ls_int, K):
    ls_max = []
    for a,b in ls_int:
        if a==0:
            ls_max.append(b-1)
        elif b == (K+1):
            ls_max.append(K-a)
        else:
            ls_max.append((b-a)//2)

    ls_max = sorted(ls_max)

    if not ls_max:
        return 0.
    elif len(ls_max)==1:
        return ls_max[0]/K
    else:
        return (ls_max[-1] + ls_max[-2])/K

def gen_sol(ls_P, K):
    #return 0.
    ls_int = [(a, b)  for a,b in zip(ls_P,ls_P[1:])]
    if 1 not in ls_P:
        ls_int.append((0, ls_P[0]))
    if K not in ls_P:
        ls_int.append((ls_P[-1], K+1))

    # Escenario 1: elegimos los dos números en el
    # mismo intervalo
    sol1 = gen_esc1(ls_int, K)
    # Escenario 2: elegimos los dos números en
    # distintos intervalos
    sol2 = gen_esc2(ls_int, K)

    return max(sol1, sol2)

for i in range(T):
    N, K = [int(x) for x in input().split()]
    st_P = {int(x) for x in input().split()}
    ls_P = sorted(st_P)
    sol = gen_sol(ls_P, K)
    print(f'Case #{i+1}: {sol}')
