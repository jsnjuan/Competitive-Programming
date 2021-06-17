def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def dig1(x):
    return x//10

def dig2(x):
    return x%10

def trivial(num, denom):
    return num%10==0 and denom%10==0

def cancel(a, b):
    if dig1(a) == dig1(b):
        return dig2(a)*b == dig2(b) * a
    if dig2(a) == dig2(b):
        return dig1(a)*b == dig1(b) * a
    if dig1(a) == dig2(b):
        return dig2(a)*b == dig1(b) * a
    if dig2(a) == dig1(b):
        return dig1(a)*b == dig2(b) * a
    return False

ls_2digs = [i for i in range(10, 100)]
ls_nums =[]
for num in ls_2digs:
    for denom in ls_2digs:
        if cancel(num, denom) and not trivial(num, denom) and num/denom < 1:
            print('{}/{}'.format(num, denom))
            ls_nums.append( (num, denom) )

print(ls_nums)

num_total=1
for a, _ in ls_nums:
    num_total*=a

denom_total=1
for _, b in ls_nums:
    denom_total*=b

gcd_nd = gcd(num_total, denom_total)
print( '{}/{}'.format( num_total//gcd_nd, denom_total//gcd_nd) )
