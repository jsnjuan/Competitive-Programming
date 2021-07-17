
T = int(input())

def gen_options(grid):
    st_sols = set()
    for (r1, c1), (r2, c2) in [((0, 1),(2, 1)),
                               ((0, 2),(2, 0)),
                               ((1, 0),(1, 2)),
                               ((0, 0),(2, 2))]:
        a, b = grid[r1][c1], grid[r2][c2]
        sols = set()
        if (b-a)%2==0:
            sols={a + (b-a)//2}
        st_sols|=sols
    return st_sols

def is_seq(a, b, c):
    d1 = b-a
    d2 = c-b
    return int(d1==d2)

def count_seqs(ngrid):
    sol = 0
    for row in range(3):
        sol = sol + is_seq(*ngrid[row])
    for col in range(3):
        sol = sol + is_seq(ngrid[0][col],ngrid[1][col], ngrid[2][col])

    sol = sol + is_seq(ngrid[0][0],ngrid[1][1], ngrid[2][2])
    sol = sol + is_seq(ngrid[2][0],ngrid[1][1], ngrid[0][2])
    return sol

def gen_sol(grid):
    st_options = gen_options(grid)
    sol = 0
    #print('all options are:', st_options)
    for opt in st_options:
        grid[1][1] = opt
        nsol = count_seqs(grid)
        if nsol>sol:
            sol = nsol
    return sol

for t in range(1, T+1):
    grid = []
    for row in range(3):
        row_cad = input().split(' ')
        row_ls = [int(x) for x in row_cad]
        if row==1:
            row_ls = [row_ls[0], None, row_ls[1]]
        grid.append(row_ls)

    print(f'Case #{t}:', gen_sol(grid))
