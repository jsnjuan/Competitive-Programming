
def gen_sol(S, N, K):

    # Tomamos la mitad de la cadena, que incluye el caracter
    # de enmedio si la cadena es de longitud impar
    ss = S[:(N+1)//2]

    #Tenemos dos casos:

    # Caso I: el número de subcadenas menor lexicográficamente que ss

    n1 = 0

    p = len(ss) - 1
    for c in ss:
        n1 = n1 + (ord(c)-97)*pow(K, p, 10**9 + 7)
        n1 = n1%(10**9 + 7)
        p = p-1


    # Caso II: la subcadena ss es igual, en este caso hay que invertir
    # manualmente la cadena para ver si es palíndromo o no
    if len(S)%2==0:
        ss2 = S[:N//2] + S[:N//2][::-1]
    else:
        ss2 = S[:N//2] + S[N//2]+S[:N//2][::-1]

    n2 = 1 if ss2 < S else 0

    return (n1 + n2)%(10**9 + 7)

T = int(input())

for i in range(T):
    N, K = [ int(x) for x in input().split()]
    S = input()

    sol = gen_sol(S, N, K)

    print(f'Case #{i+1}:', sol)
