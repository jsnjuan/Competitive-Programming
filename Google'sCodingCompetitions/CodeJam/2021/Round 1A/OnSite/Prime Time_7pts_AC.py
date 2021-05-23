from functools import reduce

T = int(input())

def suma(ls):
    return sum(ls)
    
def prod(ls):
    return reduce(lambda x, y: x*y, ls)

def gen_sol(ls):
    sol = 0
    n = len(ls)
    for i in range(1, (1<<n)-1):
        #print( bin(i)[2:].zfill(n))
        mask = bin(i)[2:].zfill(n)
        c1, c2 = [], []
        for j, b in enumerate(mask):
            if b=='0':
                c1.append(ls[j])
            else:
                c2.append(ls[j])
        suma_c1 = suma(c1)
        prod_c2 = prod(c2)
        if suma_c1 == prod_c2:
            if suma_c1 > sol:
                sol = suma_c1
            
    return sol


for i in range(T):
    M = int(input())
    
    ls = []
    
    for j in range(M):
        P, N = input().split(' ')
        P, N = int(P), int(N)
        ls.extend([P]*N)
    
    sol = gen_sol(ls)
    print(f'Case #{i+1}: {sol}')
        