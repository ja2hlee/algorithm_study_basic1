n, s, m = map(int, input().split())
vol_dif = list(map(int, input().split()))

dp = [[] for _ in range(n+1)]
dp[0].append(s)

for i in range(n):
    for vol in dp[i]:
        if vol + vol_dif[i] <= m:
            dp[i+1].append(vol+vol_dif[i])
        if vol - vol_dif[i] >= 0:
            dp[i+1].append(vol-vol_dif[i])
    
    dp[i+1] = list(set(dp[i+1])) #같은 값이 들어가지 않도록

if dp[n]:
    print(max(dp[n]))
else:
    print(-1)

