from bisect import bisect_right
from math import sqrt

def pal(i):
    return str(i) == str(i)[::-1]

pal_1d = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
pal_2d = {f'{i}{i}' for i in pal_1d}

pal_3d = {f'{i}{j}{i}' for i in pal_1d for j in pal_1d}

pal_4d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_2d}|
          {f'{i}{i}' for i in pal_2d})

pal_5d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_3d}|
          {f'{i}{j}{i}' for i in pal_2d for j in pal_1d})

pal_6d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_4d}|
          {f'{i}{j}{i}' for i in pal_2d for j in pal_2d}|
          {f'{i}{i}' for i in pal_3d})

pal_7d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_5d}|
          {f'{i}{j}{i}' for i in pal_2d for j in pal_3d}|
          {f'{i}{j}{i}' for i in pal_3d for j in pal_1d})

pal_8d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_6d}|
          {f'{i}{j}{i}' for i in pal_2d for j in pal_4d}|
          {f'{i}{j}{i}' for i in pal_3d for j in pal_2d}|
          {f'{i}{i}' for i in pal_4d})

pal_9d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_7d}|
          {f'{i}{j}{i}' for i in pal_2d for j in pal_5d}|
          {f'{i}{j}{i}' for i in pal_3d for j in pal_3d}|
          {f'{i}{j}{i}' for i in pal_4d for j in pal_1d})

pal_10d = ({f'{i}{j}{i}' for i in pal_1d for j in pal_8d}|
          {f'{i}{j}{i}' for i in pal_2d for j in pal_6d}|
          {f'{i}{j}{i}' for i in pal_3d for j in pal_4d}|
          {f'{i}{j}{i}' for i in pal_4d for j in pal_2d}|
          {f'{i}{i}' for i in pal_5d})

pals = pal_1d|pal_2d|pal_3d|pal_4d|pal_5d|pal_6d|pal_7d|pal_8d|pal_9d|pal_10d
pals = {int(p) for p in pals if pal(int(p))}

pals = pals-{0}
pals = sorted(pals)

T = int(input())

def gen_sol(A):
    pos = bisect_right(pals, A)
    st = set()
    for i in range(pos):
        p = pals[i]
        if (A%p)==0:
            st.add(p)
    return len(st)

for n in range(T):
    A = int(input())
    sol = gen_sol(A)
    print(f'Case #{n+1}: {sol}')
