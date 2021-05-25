# Definición de funciones

def genera_contador(cad):
    dic = {}
    for l in cad:
        dic[l] =  dic.get(l, 0) + 1
    return dic

def calcula_num(cad):
    
    ls_sol = []

    dic_sol = {'Z':0 , 'W': 2, 'U': 4, 'X': 6, 'G': 8, 
               'O': 1, 'T': 3, 'F': 5, 'S': 7, 'E': 9}

    contador = genera_contador(cad)

    ls1 = [('Z', 'ZERO'), ('W', 'TWO'), ('U', 'FOUR'), ('X', 'SIX'), 
           ('G', 'EIGHT'), ('O', 'ONE'), ('T', 'THREE'), ('F', 'FIVE'), 
           ('S', 'SEVEN'), ('E', 'NINE')]
    
    for clave, letra in ls1:
        if clave in contador and contador[clave] > 0:
            veces = contador[clave]
            ls_sol.extend([dic_sol[clave]] * veces)
            for l in letra:
                contador[l] -= veces
   
    ls_sol.sort()
    return ls_sol

# Inicia el programa

T = int(input())

for i in range(T):
    # Ya se lee la cadena
    cad = input()
    sol = calcula_num(cad)
    sol_cad = ''.join([str(n) for n in sol])

    print('Case #{}:'.format(i+1), sol_cad)