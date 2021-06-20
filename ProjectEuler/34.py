
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def gen_sum_digits_fct(n):
    sol = 0
    for d in str(n):
            sol += factorial[int(d)]
    return sol

# Upper limit: 7 * 9! ~2,540,160
ls =[]
for i in range(3, 2_540_160 + 1):
    sum_digits_fct = gen_sum_digits_fct(i)
    #if '9' in str(i):
    if i== sum_digits_fct:
        print(f'i = {i}, sum_digits={sum_digits_fct}')
        ls.append(i)

print('Solution:', sum(ls))
