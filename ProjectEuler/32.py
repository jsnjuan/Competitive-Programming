from itertools import combinations, permutations

def conv(t):
    return int( ''.join(t))

def gen_cands(m1, m2, p):
    st = set()
    for pm1 in permutations(m1):
        for pm2 in permutations (m2):
            for pp in permutations(p):
                if conv(pm1) * conv(pm2)  == conv(pp):
                    st.add(tuple(sorted([pm1, pm2, pp])))

    return st

# Lets take all nine digits:
all_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

cnt=0
st_n_digits = set()
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
             if (i+j+k)==9:
                 # first we take  i elements,
                 # then  j elements, and the rest is k
                 print(i, j, k)
                 st_n_digits.add((i, j, k))

print('There are',len(st_n_digits), 'distinct ways to take digits to form '
      'multiplicand, multiplier and product')

print(st_n_digits)
# So far, this code gave us the combinations of distinct digits
# we should take for each value (multiplicand, multiplier and product)

st_sols = set()

for a, b, c in st_n_digits:
    for multiplicand in combinations(all_digits, a):
        all_digits2 = all_digits - set(multiplicand)
        for multiplier in combinations(all_digits2, b):
            product = all_digits2 - set(multiplier)
            st_sols |= gen_cands( multiplicand, multiplier, product)

print(len(st_sols))
print(st_sols)

#Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
sol=0

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
for p in {x for _, _, x in st_sols}:
    sol += conv(p)
print('Solution is:', sol)
