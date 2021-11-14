T = int(input())

def gen_sol(S, N, D, C, M):

    all_dogs = S.count('D')
    for a in S:
        if a == 'D':
            if D>0:
                all_dogs = all_dogs-1
                D-=1
                C+=M
            else:
                break
        else:
            if C>0:
                C-=1
            else:
                break
    dc_sol = {True:'YES'}
    return dc_sol.get(all_dogs == 0, 'NO')

for i in range(T):
    cad = input()
    N, D, C, M = [int(x) for x in cad.split(' ')]
    S = input()
    sol = gen_sol(S, N, D, C, M)
    print(f"Case #{i+1}: {sol}")

