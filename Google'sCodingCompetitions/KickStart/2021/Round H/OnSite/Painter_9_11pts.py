T = int(input())

def gen_sol(N, P):
    dc_colors = {
    'U':set(),
    'R':{'R'},
    'Y':{'Y'},
    'B':{'B'},
    'O':{'R', 'Y'},
    'P':{'R', 'B'},
    'G':{'Y', 'B'},
    'A':{'R', 'Y', 'B'}
    }

    ls = [dc_colors[p] for p in P]

    # Vamos por pasadas, serían U, R, Y, B
    # Veamos cuantas pasadas de red ocupamos
    i = 0
    sol = 0
    while i < N:
        if len(ls[i]):
            if 'R' in ls[i]:
                ls[i] = ls[i] - {'R'}
                sol +=1
                j = i+1
                while j<N and 'R' in ls[j]:
                    ls[j] = ls[j] - {'R'}
                    j+=1

            if 'Y' in ls[i]:
                ls[i] = ls[i] - {'Y'}
                sol +=1
                j = i+1
                while j<N and 'Y' in ls[j]:
                    ls[j] = ls[j] - {'Y'}
                    j+=1

            if 'B' in ls[i]:
                ls[i] = ls[i] - {'B'}
                sol +=1
                j = i+1
                while j<N and 'B' in ls[j]:
                    ls[j] = ls[j] - {'B'}
                    j+=1
        i+=1
    return sol

for i in range(T):
    N = input()
    N = int(N)
    P = input()

    sol = gen_sol(N, P)
    print(f"Case #{i+1}: {sol}")
