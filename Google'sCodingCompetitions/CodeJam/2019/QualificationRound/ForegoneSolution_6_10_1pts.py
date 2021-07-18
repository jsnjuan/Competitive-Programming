def gen_sol(n):
    a = list(n)
    b = ['0' for _ in range(len(n))]
    
    for i, digit in enumerate(n):
        if digit == '4':
            a[i] = '3'
            b[i] = '1'
    
    return ''.join(a), ''.join(b)


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n = input() # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, *gen_sol(n)))