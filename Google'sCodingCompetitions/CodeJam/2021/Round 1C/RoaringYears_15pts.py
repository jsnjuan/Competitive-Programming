# Generemos los numeros roraring de uno a un millon
# Y veamos algún patrón

from bisect import bisect_right

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def gen_num(i, j):
    ls = [ str(i + inc) for inc in range(j)]
    return int(''.join(ls))

st = set()
for i in range(1, 10_000):
    for j in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
        st.add(gen_num(i, j))

ls  = sorted(st)

T = int(input())

for i in range(T):
    Y = int(input())
    sol = find_gt(ls, Y)
    print(f'Case #{i+1}: {sol}')
