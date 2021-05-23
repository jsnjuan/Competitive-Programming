# Modulos
import sys

def calcula_sol():
    tbl = {(2, 2): [(1, 1), (1, 2), (1, 3), 
                        (2, 1), (2, 2), (2, 3), 
                        (3, 1), (3, 2), (3, 3)],
           (2, 3): [(1, 4), (2, 4), (3, 4)], 
           (4, 2): [(4, 1), (4, 2), (4, 3), 
                    (5, 1), (5, 2), (5, 3)],
           (4, 3): [(4, 4), (5, 4)]}

    for centro in tbl:
        ls = tbl[centro]
        while ls:
            print(*centro)
            sys.stdout.flush()

            # se lee la respuesta del juez
            #rg, cg = input(), input()
            cad = input()
            x, y = map(int, cad.split(' '))
            r_c = x, y
            if not sum(r_c):
                return
            if r_c in ls:
                ls.remove(r_c)

            #print(tbl)
    # Fin
    return


T = int(input())

for _ in range(T):
    A = input()
    calcula_sol()