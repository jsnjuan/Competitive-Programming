T = int(input())

def eval_pos(N, mid, rest):
    pref = N[:mid]
    #print(f'evaluating N = {N}, mid = {mid}, pref = {pref}, rest = {rest}')
    return pref=='' or any(int(c)>rest for c in pref)

def gen_best_pos(N, rest):
    for i, c in enumerate(N):
        if int(c) > rest:
            return N[:i] + str(rest) + N[i:]
    return N + str(rest)

def gen_sol(N):
    sum_N = sum([ int(c) for c in N])
    if sum_N % 9 > 0:
        rest = 9 - (sum_N % 9)
    else:
        rest = 0
        return N[:1] + '0' + N[1:]

    sol =gen_best_pos(N, rest)
    return sol

for n in range(T):
    N = input()
    sol = gen_sol(N)
    print(f'Case #{n+1}: {sol}')
