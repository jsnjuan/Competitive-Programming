def gen_ls(N, C):
    if C<(N-1) or C>(N*(N-1)//2 + N-1):
        return []
    if N==2:
        return {1:[1, 2], 2:[2, 1]}.get(C, [])
    # Vemos si existe una lista de menor tamaño
    ls = gen_ls(N-1, C-1)
    if ls:
        return ls + [N]

    # Si no, entonces generamos la máxima que se puede de tamaño anterior,
    # ya sabemos que es de tamaño N-1 y de costo N*(N-1)/2 - 1
    ls = gen_ls(N-1, N*(N-1)//2-1)

    if ls:
        # Tenemos que insertar N, la posición de N será
        i =  C - (N*(N-1)//2-1 + 1)
        pos = i//2 if i%2 else N - i//2 - 1
        ls.insert(pos, N)
        return ls
    else:
        return []

T = int(input())
#T = 0
for i in range(T):
    N, C = input().split()
    N, C = int(N), int(C)
    sol = gen_ls(N, C)
    if sol:
        print(f'Case #{i+1}:', ' '.join( str(y) for y in sol))
    else:
        print(f'Case #{i+1}: IMPOSSIBLE')
