# Source:
# sum two tuples: https://stackoverflow.com/a/12702871
# dfs/bfs in python: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

t = int(input()) # read a line with a single integer

def neighbors(n, path, node,edges_restricted):
    # Possible neighbors are generated going only 
    # south or east, so we validate they are 
    # valid paths
    v1 = tuple(map(lambda x, y: x + y, node, (1, 0)))
    p1 = path +  'S'
    v2 = tuple(map(lambda x, y: x + y, node, (0, 1)))
    p2 = path +  'E'

    ls = []

    if (node, v1) not in edges_restricted and v1[0] < n and v1[1] < n:
        ls.append((p1, v1))
    if (node, v2) not in edges_restricted and v2[0] < n and v2[1] < n:
        ls.append((p2, v2))

    return ls

def gen_edges_restricted(P):
    st = set()
    ini = 0, 0
    for movement in P:
        if movement == 'S':
            nxt = tuple(map(lambda x, y: x + y, ini, (1, 0)))
        else:
            nxt = tuple(map(lambda x, y: x + y, ini, (0, 1)))   
        st.add((ini, nxt))
        ini = nxt
    return st

def gen_sol(n, P):

    edges_restricted = gen_edges_restricted(P)

    ini = 0, 0
    fin = n - 1, n - 1

    visited, stack = set(), [('',ini)]

    path = None
    
    while True:
        path, node = stack.pop()
        if fin == node:
            break
        if node not in visited:
            visited.add(node)
            ls_vs = neighbors(n, path, node,edges_restricted)
            stack.extend(ls_vs)
    
    return path

for i in range(1, t + 1):
  n = int(input()) # read a list of integers, 2 in this case
  P = input()
  print("Case #{}: {}".format(i, gen_sol(n, P)))