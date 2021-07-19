# ProjectEuler.net
# Problem 39: Integer right triangles

# Equations we have:
# a + b + c = p
# leting c be the max(a, b, c) we hace
# a^2 + b^2 = c^2
# Then
# a+b + (a^2 + b^2)**0.5 = p
# leting b as a function of 'a' we have:
# a^2 + b^2 = (p - a - b)^2
# a^2 = (p-a)^2 - 2*(p-a)*b
# b = [ (p-a)^2 - a^2 ]/[ 2*(p-a)]
# b = (p-a)/2 - a^2/2*(p-a)

from math import sqrt

def gen_sols(p):
    nsol = 0
    lsols = []
    for a in range(1, p):
        b = (p-a)//2 - a*a//(2*(p-a))
        c = sqrt(a*a + b*b)
        c = int(c)
        cond1 = a>0 and b>0 and c>0
        cond2 = (a*a + b*b)==c*c
        cond3 = (a+b+c)==p
        cond4 = c>a and c>b
        cond5 = tuple(sorted((a, b, c))) not in lsols
        if cond1 and cond2 and cond3 and cond4 and cond5:
            nsol +=1
            lsols.append(tuple(sorted((a, b, c))))
    return nsol

max_p = None
n_sols_p = 0
for p in range(1,1_000 + 1):
    sols = gen_sols(p)
    if sols>n_sols_p:
        n_sols_p = sols
        max_p = p

print(f'p that maximizes solutions is: {max_p}, # solutions: {n_sols_p}')
