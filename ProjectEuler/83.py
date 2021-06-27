from heapq import heappush, heappop

def gen_matrix():
    M = []
    #with open(r'p083_matrix_prueba.txt') as  mx_file:
    with open(r'p083_matrix.txt') as  mx_file:
        for line in mx_file.readlines():
            M.append([int(x) for x in line.split(',')])

    return M

def gen_min_dists(M, N=80):
    D = [[0]*N for _ in range(N)]
    mark = [[0]*N for _ in range(N)]
    pq = []

    # We push top left corner into the priority queue
    heappush( pq, (M[0][0], (0, 0)))

    while(pq):
        # We take the least value
        (v, (x, y)) = heappop(pq)
        # If it is already marked we continue
        if mark[x][y]:
            continue

        # Generate the min distante until this node
        D[x][y] = v
        # mark the node
        mark[x][y] = 1
        # Visit neighboors
        for dx, dy in zip([0, -1, 0, 1], [-1, 0, 1, 0]):
            if (x+dx)>=0 and (x+dx)<N and (y+dy)>=0 and (y+dy)<N and mark[x+dx][y+dy]==0:
                ndist = D[x][y] + M[x+dx][y+dy]
                heappush(pq, (ndist, (x+dx, y+dy)))
    return D

M = gen_matrix()
#print(*M, sep='\n')
max_matrix = max(x  for ls in M for x in ls)
print('Maximum matrix value:', max_matrix)
print("Maximum sum value (80*80*max_matrix_value) :", 80*80*max_matrix )

# Generate minimum distances matrix

# Test case
#D = gen_min_dists(M, N=5)
D = gen_min_dists(M, N=80)
#print('Solution:',  D[4][4])
print('Solution:', D[79][79])
