T = int(input())

def gen_st(a, b, N):
    ls = []
    mx=N
    while mx<=a:
        ls.append(mx)
        a = a-mx
        mx = mx-1
    if a>0:
        ls.append(a)
    return '{}\n{}'.format(len(ls), ' '.join(str(n) for n in ls) )

def gen_sol(N, X, Y):
    if (Y*N*(N+1) % (2*(X+Y)))== 0:
        b = (Y*N*(N+1)) // (2*(X+Y))
        a = N*(N+1)//2 - b
        st = gen_st(a, b, N)
        return 'POSSIBLE' + '\n' + st
    return 'IMPOSSIBLE'

for n in range(T):
    N, X, Y = [int(t) for t in input().split()]
    sol = gen_sol(N, X, Y)
    print(f'Case #{n+1}: {sol}')
