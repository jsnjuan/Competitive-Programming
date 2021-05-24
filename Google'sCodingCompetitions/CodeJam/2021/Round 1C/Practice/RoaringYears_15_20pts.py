def bisect_right_mod(fn, Y, lo=0, hi=None):
    """
    modified bisect_right function from python bisect module to work with a
    monotonic increasing function instead of an array
    original source:
        https://github.com/python/cpython/blob/3.9/Lib/bisect.py#L15
    """
    while lo < hi:
        mid = (lo+hi)//2
        if Y < fn(mid): hi = mid
        else: lo = mid+1
    return fn(lo)

def gen_fn(n):
    def fn(x):
        ls = [str(x + inc) for inc in range(n)]
        return int(''.join(ls))
    return fn

def best_concat_n(Y, n):
    fn = gen_fn(n)
    return bisect_right_mod(fn, Y, lo=1, hi= 10 ** 20)

def gen_sol(Y):
    sol = 0
    dif_sol = 10 ** 18
    for n in range(2, 18+1):
        y_n = best_concat_n(Y, n)
        if y_n-Y<dif_sol:
            dif_sol = y_n - Y
            sol = y_n

    return sol

T = int(input())

for i in range(T):
    Y = int(input())
    sol = gen_sol(Y)
    print(f'Case #{i+1}: {sol}')
