# Este código alcanza 7pts + 13pts

T = int(input())

def valid_candidate(x, dc):
    x_or = x
    dc_ps = dc.copy()
    for p in dc_ps:
        while x%p==0:
            x/=p
            dc_ps[p]-=1
            if dc_ps[p] < 0:
                return False
    if x > 1:
        return False

    valid = sum(a*b for a, b in dc_ps.items()) == x_or
    return valid

def gen_sol(dc_ps):
    sol = 0
    # x representa la suma que podemos lograr de los
    # factores, x es como tal el número que debemos
    # comprobar si es factorizable con los primos
    # proporcionados
    for x in range(50_000):
        valid_x = valid_candidate(x, dc_ps)
        if valid_x and x > sol:
            sol = x
    return sol

for i in range(T):
    M = int(input())
    dc_ps = {}
    for j in range(M):
        P, N = input().split(' ')
        P, N = int(P), int(N)
        dc_ps[P] = N
    sol = gen_sol(dc_ps)
    print(f'Case #{i+1}: {sol}')
