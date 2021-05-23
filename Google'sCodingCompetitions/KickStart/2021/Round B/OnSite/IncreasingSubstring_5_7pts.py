T = int(input())

for i in range(T):
    N = int(input())
    S = input()
    S = 'Z' + S
    sol = [0 for _ in range(N+1)]

    for j in range(1, N+1):
        if S[j]>S[j-1]:
            sol[j] = sol[j-1] + 1
        else:
            sol[j] = 1

    print(f'Case #{i+1}:', *sol[1:])
