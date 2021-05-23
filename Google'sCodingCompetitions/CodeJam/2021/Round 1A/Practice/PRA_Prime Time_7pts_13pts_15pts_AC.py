# Hacemos cambios para que alcance el test más grande

T = int(input())

def valid_candidate(y, dc, total):
    x = total - y
    dc_ps = dc #.copy()
    sum_ps_x = 0
    for p in dc_ps:
        cnt = 0
        while x%p==0:
            x//=p
            sum_ps_x += p
            cnt+=1
        if cnt>dc_ps[p]:
            return False

    return (x==1) and (sum_ps_x == y)

def gen_sol(dc_ps, total):
    sol = 0
    # En este caso, x no representa lo mismo que
    # en el caso anterior,
    for x in range(2, 30_000):
        if (total - x)<=1:
            break
        if valid_candidate(x, dc_ps, total):
            return total - x
    return 0

for i in range(T):
    M = int(input())
    dc_ps = {}
    total = 0
    for j in range(M):
        P, N = input().split(' ')
        P, N = int(P), int(N)
        dc_ps[P] = N
        total += P*N
    sol = gen_sol(dc_ps, total)
    print(f'Case #{i+1}: {sol}')
