uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special = '#@*&'

T = int(input())

def fix_cond2(s):
    for l in uppercase:
        if l in s:
            return s
    return s + 'A'

def fix_cond3(s):
    for l in lowercase:
        if l in s:
            return s
    return s + 'a'

def fix_cond4(s):
    for d in digits:
        if d in s:
            return s
    return s + '0'

def fix_cond5(s):
    for c in special:
        if c in s:
            return s
    return s + '#'

def fix_cond6(s):
    n = len(s)
    if n<7:
        return s + 'A'*(7-n)
    return s

def gen_sol(old_pass):
    npass = fix_cond2(old_pass)
    npass = fix_cond3(npass)
    npass = fix_cond4(npass)
    npass = fix_cond5(npass)
    npass = fix_cond6(npass)
    return npass

for n in range(T):
    _ = input()
    old_pass = input()
    sol = gen_sol(old_pass)
    print(f'Case #{n+1}: {sol}')
