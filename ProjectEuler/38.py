# ProjectEuler.net
# Problem 38: Pandigital multiples

# Upperbound for i: i is the number which is multiplied by 1, 2, 3... n,
# so, if n should be at minimum 2, i should be at most 5 digits
# upperbound for n: n is the maximum number of the tuple (1, 2, ..., n),
# which is the series of numbers that are multipled by i, and then their results
# are concatenated, so, by initial condition n>2, and in the case of single
# digit number i, n will be 9 as maximum value
#

def gen_pand(i, n):
    cad_prod = ''
    for j in range(1, n+1):
        cad_prod += str(j*i)
    if len(cad_prod)!=9:
        return False, None
    for i in range (1, 10):
        if cad_prod.count(str(i))!=1:
            return False, None
    return True, cad_prod

largest_pand_9_digit = 0
largest_i = None
largest_n = None
for i in range (1, 100_000):
    for n in range(2, 10):
        band, pand_i_n = gen_pand(i, n)
        if band and int(pand_i_n) > largest_pand_9_digit:
            largest_pand_9_digit =int(pand_i_n)
            largest_n = n
            largest_i = i

print(f'Largest 1 to 9 pandigital 9-digit number that can be formed as the '
      f'concatenated product of an integer ({largest_i}) with (1,2, ... , {largest_n}) where '
      f'n > 1 is {largest_pand_9_digit}')
