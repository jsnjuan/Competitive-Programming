
T = int(input())

def gen_sol(X, Y, S):
    #eliminamos duplicados
    s = ''.join('' if a==b else a for a, b in zip(S,'*' + S))
    #print('no dup:', s.split('?'))
    sol = 0

    if s.startswith('?C'):
        s = s.replace('?C', 'CC')
    if s.startswith('?J'):
        s = s.replace('?J', 'JJ')
    if s.endswith('C?'):
        s = s.replace('C?', 'CC')
    if s.endswith('J?'):
        s = s.replace('J?', 'JJ')

    s = s.replace('C?C', 'CCC')
    s = s.replace('J?J', 'JJJ')

    s = s.replace('C?J', 'CCJ')
    s = s.replace('J?C', 'JJC')

    return s.count('CJ')*X + s.count('JC')*Y

    return sol

for i in range(T):
#T = 0
    X, Y, S = input().split()
    X, Y = int(X), int(Y)

    sol = gen_sol(X, Y, S)

    print(f'Case #{i+1}: {sol}')
