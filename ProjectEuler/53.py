# 53.py
N = 100 + 1
C = [ [0 for _ in range(N+1)] for _ in range(N+1)]

C[1][1] = 1
for i in range(N+1):
    C[i][0] = 0
for i in range(N):
    C[i][i+1] = 0

cnt = 0
for i in range(2, N+1):
    for j in range(1, i+1):
        #C[i][j] = C[i-1][j-1] + C[i-1][j]
        C[i][j] = min(C[i-1][j-1] + C[i-1][j], 1_000_001)
        if C[i][j]>=1_000_000:
            cnt +=1

# We can print pascal triangle
#for i in range(N+1):
#    print( ' '.join('{:7d}'.format(d) for d in C[i]))

print('Sol:', cnt)
