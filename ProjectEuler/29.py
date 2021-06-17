st_ab = set()
for a in range(2, 100+1):
    for b in range(2, 100+1):
        st_ab.add(a**b)

print(len(st_ab))
