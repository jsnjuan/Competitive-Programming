T = int(input())

for i in range(1, T+1):
    NS = input()
    N, S = [ int(x) for x in NS.split(' ')]
    dc_skills = {}
    for ii in range(N):
        st_skills = set([int(x) for x in input().split(' ')][1:])
        dc_skills[ii] = st_skills
        #print(ii, st_skills)

    st = set()
    for ii in range(N):
        for jj in range(N):
            if ii != jj and (dc_skills[ii] - dc_skills[jj]):
                st.add((ii, jj))

    print('Case #{}: {}'.format(i, len(st)))
