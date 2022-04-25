from math import pi

T = int(input())

def gen_sol(R, A, B):
    sol=0.
    rght=True
    # Draw first circle
    sol += pi*R*R
    # loop algorithm
    while R>0:
        if rght:
            R = R*A
        else:
            R = R//B
        sol += pi*R*R
        rght = not rght
    return sol

for n in range(T):
    R, A, B = [int(t) for t in input().split()]
    sol = gen_sol(R, A, B)
    print(f'Case #{n+1}: {sol}')
