import itertools

def gen_sol(LL, N):
    sol=0
    # Creamos los 4 diccionarios necesarios
    val_pos = dict(zip(LL, range(1, N+1)))
    pos_val = {b:a for a, b in val_pos.items()}

    # Generemos los diccionarios de los valores a la
    # derecha y a la izquierda de cada número
    der = dict([(x, y) for x, y in zip(LL, LL[1:])])
    izq = dict([(x, y) for x, y in zip(LL[1:], LL)])

    for i in range(1, N):
        #print(f'Iteración {i}:')
        if i == pos_val[i]:
            sol +=1
        else:
            a, pos_a = pos_val[i], i
            b, pos_b = i, val_pos[i]

            #print(f'a = {a}, pos_a={pos_a}')
            #print(f'b = {b}, pos_a={pos_b}')

            sol+=  pos_b - pos_a + 1

            der_a, izq_a = der.get(a, None), izq.get(a,None)
            der_b, izq_b = der.get(b, None), izq.get(b, None)

            izq[ der_b ] = a

            nder = {}
            sig = b
            ls = [b]
            while sig!=a:
                nder[sig] = izq[sig]
                sig = izq[sig]
                ls.append(sig)

            nder[a] = der.get(b, None)

            nizq  = {}
            ant = a
            while ant!=b:
                nizq[ant] = der[ant]
                ant = der[ant]

            nizq[b] = izq.get(a, None)

            der.update(nder)
            izq.update(nizq)

            # Actualizamos posiciones
            for n, x in enumerate(ls):
                val_pos[x] = i + n

            pos_val = {b:a for a, b in val_pos.items()}

    return sol

def gen_sol2(N, C):
    L = [i for i in range(1, N+1)]
    for ls in itertools.permutations(L):
        if gen_sol(ls, N) == C:
            return ' '.join([str(i) for i in  ls])
    return ''

T = int(input())
#T = 0
for i in range(T):
    N, C = input().split()
    N, C = int(N), int(C)
    sol = gen_sol2(N, C)
    if sol:
        print(f'Case #{i+1}: {sol}')
    else:
        print(f'Case #{i+1}: IMPOSSIBLE')
