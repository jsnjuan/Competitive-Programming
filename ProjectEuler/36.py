def palindromic(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True

sol = 0
for i in range(1, 1_000_000):
    if palindromic(str(i)) and palindromic(bin(i)[2:]):
        sol += i

print('Solution:', sol)
