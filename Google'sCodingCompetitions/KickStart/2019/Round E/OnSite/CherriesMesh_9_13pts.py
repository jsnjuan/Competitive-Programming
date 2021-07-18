T = int(input())

# codigo tomado de aquí
# https://algocoding.wordpress.com/2014/09/25/union-find-data-structure-disjoint-set-data-structure-part-2/
class UnionFind:
    """
    Class that implements the union-find structure with
    union by rank and find with path compression
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

    #def printParent(self):
        #print("index: ",list(range(9)))
        #print("parent: ", self.parent, sep='')

for t in range(1, T+1):
    NM = input().split(' ')
    N, M = [int(x) for x in NM]

    uf = UnionFind(N)

    for _ in range(M):
        ab = input().split(' ')
        a, b = [int(x) for x in ab]
        uf.union(a-1, b-1)

    myDict = {}
    for node in range(N):
        root = uf.find(node)
        if not root in myDict:
            myDict[root] = set([node])
        else:
            myDict[root].add(node)

    black_strands = 0
    for mySet in myDict.values():
        black_strands += len(mySet) - 1

    if black_strands >= N-1:

        print('Case #{}: {}'.format(t, N-1))
    else:
        print('Case #{}: {}'.format(t, black_strands + (N-1 - black_strands) * 2))
        
        