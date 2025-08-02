import sys
input = sys.stdin.readline 

n = int(input())
T=[]; P=[];

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0]*(n+1)

for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])
    #오늘과 내일을 비교해서 최대수익 저장
    
    if i+T[i] <= n:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
        #dp[i+T[i]]상담이 끝나는 시간에 대한 날짜 계산

print(max(dp))