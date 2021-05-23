T = int(input())

for i in range(T):
    N, K = [int(x) for x in input().split()]
    S = input()
    goodness = 0
    for j in range(0, N//2):
        goodness += int(S[j]!=S[N-j-1])
    sol = abs(goodness - K)
    print(f'Case #{i+1}: {sol}')
    