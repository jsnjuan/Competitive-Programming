T = int(input())

def gen_sol(I, P):
    pos = 0
    ln_P = len(P)
    sol = 0
    for l in I:
        if pos>=ln_P:
            return "IMPOSSIBLE"
        if l == P[pos]:
            pos+=1
            continue
        while pos<ln_P and P[pos]!=l:
            pos+=1
            sol+=1
        if pos>=ln_P:
            return "IMPOSSIBLE"
        if pos<ln_P and l!=P[pos]:
            return "IMPOSSIBLE"
        if pos<ln_P and l==P[pos]:
            pos +=1
    sol += ln_P - pos
    return f'{sol}'


for n in range(T):
    I = input()
    P = input()
    sol = gen_sol(I, P)
    print(f'Case #{n+1}: {sol}')
