
def valor(cad):
    d, sol = 1, 0
    for l in cad:
        if l == 'C':
            d *= 2
        else:
            sol += d
    return sol

def actualiza_cad(cad):
    # Quitamos las utimas C's, hallando la ultima S
    cad2 = cad[:cad.rfind('S') + 1]
    ind = cad2.rfind('C')
    #cad[ind : ind + 1] = 'SC' # intercambiamos
    return cad[:ind] + 'SC' + cad[ind+2:]

def calcula_sol(D, cad):
    # Sin solucion, existen al menos D + 1 disparos
    if tuple(cad).count('S') > D:
        return 'IMPOSSIBLE'
    sol = 0
    while( valor(cad)>D ):
        cad = actualiza_cad(cad) # actualiza de la manera + optima
        sol += 1
    return sol

#Programa
T = int(input())

for case in range(T):
    D, cad = input().split(' ')
    D = int(D)
    print('Case #{}: {}'.format(case + 1, calcula_sol(D, cad)))
