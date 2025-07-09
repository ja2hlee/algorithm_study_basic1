def tricorn(k):
    Tn_list = []
    n =1
    while True:
        Tn = n*(n+1)/2
        if Tn > k:
            break
        Tn_list.append(Tn)
        n+=1
    
    #삼각수 합으로 표현 가능 여부 찾기 (중복 허용)
    for i in Tn_list:
        for j in Tn_list:
            for l in Tn_list:
                if i + j + l == k:
                    return 1
    return 0


t = int(input())

for _ in range(t):
    k = int(input())
    print(tricorn(k))

