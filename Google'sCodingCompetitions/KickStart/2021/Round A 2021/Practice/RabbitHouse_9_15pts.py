
#import heapq
from heapq import heappush, heappop
#h = []
#heappush(h, (5, 'write code'))
#heappush(h, (7, 'release product'))
#heappush(h, (1, 'write spec'))
#heappush(h, (3, 'create tests'))
#print(heappop(h))

def gen_sol(grid, R, C):
    sol = 0

    ls_ini = [(x, y, grid[x][y]) for x in range(R) for y in range(C)
                if grid[x][y]>0]

    marca = [[0]*C for _ in range(R)]

    # Paso 1:
    # Metemos a la cola de prioridad todos los mayores a cero
    h = []

    for x, y, v in ls_ini:
        heappush(h, (-v, (x, y) )  )

    sol = 0

    while(h):
        # Sacamos el "menor"
        (v, (x, y) ) = heappop(h)
        #print('Analizando punto:', x, y)
        # Los marcamos
        marca[x][y] = 1

        # Visitamos sus vecinos:
        for dx, dy in zip([0, -1, 0, 1], [-1, 0, 1, 0]):
        #for dy in :
            if (x+dx)>=0 and (x+dx)<R and (y+dy)>=0 and (y+dy)<C and marca[x+dx][y+dy]==0:
                if abs( -v  - grid[x+dx][y+dy])>=2:
                    fix = max(-v, grid[x+dx][y+dy]) - min(-v, grid[x+dx][y+dy]) - 1
                    grid[x+dx][y+dy] = max(-v, grid[x+dx][y+dy]) - 1
                    sol += fix
                    #print('  Ahora grid[{}][{}] = {}'.format(x+dx,y+dy,  grid[x+dx][y+dy]))
                    heappush(h,(-grid[x+dx][y+dy], (x+dx, y+dy) ))
                    #print('  Agregando a la cola ',x+dx, y+dy )
                    #print('  Hasta ahora sol vale ',sol)

    return sol

T = int(input())
#T = 0

for i in range(T):
    R, C = [int(x) for x in input().split()]
    #grid = np.zeros((R, C), dtype=int)
    grid = [ [0]*C for _ in range(R)]
    for r in range(R):
        grid[r] = [int(x)  for x in input().split()]
    #print(f"Leyendo el caso {i}")

    sol = gen_sol(grid, R, C)

    print(f'Case #{i+1}: {sol}')
