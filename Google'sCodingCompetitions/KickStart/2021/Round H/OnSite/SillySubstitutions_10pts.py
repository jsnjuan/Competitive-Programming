T = int(input())

def procesa(S):
    for i in range(0, 10):
        S = S.replace(f'{i}{(i+1)%10}', f'{(i+2)%10}')
    return S

def gen_sol(N, S):
    # Idea is to process only consecutive substrings
    S2 = S
    cnt=0
    while cnt<50:
        S2 = procesa(S)
        if S2 == S:
            break
        else:
            S = S2
    return S

for i in range(T):
    N = input()
    N = int(N)
    S = input()

    sol = gen_sol(N, S)
    print(f"Case #{i+1}: {sol}")
