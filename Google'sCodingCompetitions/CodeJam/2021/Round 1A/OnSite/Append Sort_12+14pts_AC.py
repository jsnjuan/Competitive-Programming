T = int(input())

def min_ant(elem, ant):
    if int(elem)>int(ant):
        return 0, elem
    
    if elem==ant:
        elem+='0'
        return 1, elem
    
    if ant.startswith(elem) and int(ant[len(elem):])< int('9'*len( ant[len(elem):] )):
        return len( ant[len(elem):] ), elem + str(int( ant[len(elem):] ) + 1).zfill( len( ant[len(elem):] ) )
    
    sol = 0
    while (int(elem + '0')<=int(ant)) and (int(elem + '9')<=int(ant)):
        elem+='0'
        sol+=1
    
    for i in range(10):
        if int(elem + str(i))>int(ant):
            elem +=str(i)
            break
        
    sol+=1
    return sol, elem

for i in range(T):
    N = int(input())
    ls = input().split(' ')
    ant = '0'
    sol = 0
    for elem in ls:
        movs, nant = min_ant(elem, ant)
        sol+= movs
        ant = nant
    print(f'Case #{i+1}: {sol}')
        