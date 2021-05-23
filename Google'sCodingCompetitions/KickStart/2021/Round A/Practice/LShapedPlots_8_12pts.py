
def gen_N(grid, R, C):
    N = [ [0]*C for _ in range(R)]
    N[0] = grid[0]
    for i in range(1, R):
        for j in range(C):
            N[i][j] = (N[i-1][j] + 1)*grid[i][j]
    return N

def gen_S(grid, R, C):
    S = [[0]*C for _ in range(R)]
    S[R-1] = grid[R-1]
    for i in range(R-2, -1, -1):
        for j in range(C):
            S[i][j] = (S[i+1][j] + 1)*grid[i][j]
    return S

def gen_E(grid, R, C):
    E = [[0]*C for _ in range(R)]
    for j in range(C-1, -1, -1):
        for i in range(R):
            if j==(C-1):
                E[i][C-1] = grid[i][C-1]
            else:
                E[i][j] = (E[i][j+1] + 1)*grid[i][j]
    return E

def gen_W(grid, R, C):
    W = [[0]*C for _ in range(R)]
    for j in range(0, C):
        for i in range(R):
            if j==0:
                W[i][0] = grid[i][0]
            else:
                W[i][j] = (W[i][j-1] + 1)*grid[i][j]
    return W

def gen_sol(grid, R, C):
    # Generamos las cuatro matrices
    N = gen_N(grid, R, C)
    #print('Matriz: N')
    #print(N)
    S = gen_S(grid, R, C)
    #print('Matriz: S')
    #print(S)

    E = gen_E(grid, R, C)
    #print('Matriz: E')
    #print(E)

    W = gen_W(grid, R, C)
    #print('Matriz: W')
    #print(W)

    # Calculamos los ocho tipos de L
    sol = 0
    for i in range(R):
        for j in range(C):
            # Tipo 1:   |
            #          |__
            if N[i][j]>=4 and E[i][j]>=2:
                sol += ( min( (N[i][j]//2)*2, 2*E[i][j]  )//2   ) - 1
            # Tipo 2:   __ __
            #          |

            if E[i][j]>=4 and S[i][j]>=2:
                sol += ( min( (E[i][j]//2)*2, 2*S[i][j]  ) //2  ) - 1


            # Tipo 3:   __
            #            |
            #           |
            if S[i][j]>=4 and W[i][j]>=2:
                sol += ( min( (S[i][j]//2)*2, 2*W[i][j]  ) //2  ) - 1

            # Tipo 4:
            #       __ __ |
            if W[i][j]>=4 and N[i][j]>=2:
                sol += ( min( (W[i][j]//2)*2, 2*N[i][j]  ) //2  ) - 1

            # Tipo 5:    |
            #         __|
            if N[i][j]>=4 and W[i][j]>=2:
                sol += ( min( (N[i][j]//2)*2, 2*W[i][j]  ) //2  ) - 1

            # Tipo 6:
            #        |__ __
            if E[i][j]>=4 and N[i][j]>=2:
                sol += ( min( (E[i][j]//2)*2, 2*N[i][j]  ) //2  ) - 1

            # Tipo 7:      __
            #            |
            #           |
            if S[i][j]>=4 and E[i][j]>=2:
                sol += ( min( (S[i][j]//2)*2, 2*E[i][j]  ) //2  ) - 1

            # Tipo 8:   __ __
            #               |
            if W[i][j]>=4 and S[i][j]>=2:
                sol += ( min( (W[i][j]//2)*2, 2*S[i][j] ) //2  ) - 1

    return sol

T = int(input())

for i in range(T):
    R, C = [int(x) for x in input().split()]
    #grid = np.zeros((R, C), dtype=int)
    grid = [ [0]*C for _ in range(R)]
    for r in range(R):
        grid[r] = [int(x)  for x in input().split()]
    #print(f"Leyendo el caso {i}")

    sol = gen_sol(grid, R, C)

    print(f'Case #{i+1}: {sol}')
