import string

def gen_dc_dist():
    dc_dist = {}
    cad = string.ascii_lowercase
    cad = cad + cad
    for i, l in enumerate(cad):
        for j, m in enumerate(cad):

            dc_dist[l, m] = min(abs(i-j), dc_dist.get((l, m), 1_000))
            dc_dist[m, l] = min(abs(i-j), dc_dist.get((m, l), 1_000))
    return dc_dist

dc_dist = gen_dc_dist()

def gen_sol(S, F):
    sol = 0
    for s in S:
        sol  += min(dc_dist[f, s] for f in F)
    return sol

T = int(input())

for i in range(T):
    S = input()
    F = input()
    sol = gen_sol(S, F)
    print(f"Case #{i+1}: {sol}")
