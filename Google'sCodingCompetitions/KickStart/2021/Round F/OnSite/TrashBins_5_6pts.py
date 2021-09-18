T = int(input())

def gen_sol_L(N, S):
    # always walk to the left
    sol = [0 for _ in range(N)]
    ant = -1_000_000
    for i, p in enumerate(S):
        if p=='1':
            sol[i] = 0
            ant = i
        else:
            sol[i] =  i - ant
    return sol

def gen_sol(N, S):
    sol_L = gen_sol_L(N, S)
    sol_R = gen_sol_L(N, S[::-1])[::-1]
    #print('sol_L:', sol_L)
    #print('sol_R:', sol_R)
    return sum( min(a, b) for a, b in zip(sol_L, sol_R) )


for i in range(T):
    N = int(input())
    S = input()
    sol = gen_sol(N, S)
    print(f"Case #{i+1}: {sol}")
