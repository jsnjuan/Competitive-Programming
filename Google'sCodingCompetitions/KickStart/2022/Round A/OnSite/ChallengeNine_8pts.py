T = int(input())

def cmp_min(a, b):
    for c1, c2 in zip(a, b):
        if c1 == c2:
            continue
        if int(c1) < int(c2):
            return a
        else:
            return b
    return a

def eval_pos(N, mid, rest):
    pref = N[:mid]
    #print(f'evaluating N = {N}, mid = {mid}, pref = {pref}, rest = {rest}')
    return any(int(c)>rest for c in pref)

def gen_best_pos(N, rest):
    lo = 0
    hi = len(N)+1
    while lo < hi:
        mid = (lo + hi)//2
        if mid <= lo:
            break
        #print(f'lo = {lo}, high = {hi}, mid = {mid}')
        if eval_pos(N, mid, rest):
             hi = mid-1
        else:
            lo = mid

    return N[:lo] + str(rest) + N[lo:]


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
