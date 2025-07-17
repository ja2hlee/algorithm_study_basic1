n = int(input())
T=[]; P=[];

for _ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
    
max_profit = 0
    
def profit(day, total):
    global max_profit
    if day > n:
        return #퇴사일 넘어가면 선택 자체가 불가
    max_profit = max(max_profit, total)
    
    for i in range(day, n):
        if i + T[i] <= n:
            profit(i+T[i], total+P[i])

profit(0, 0)
print(max_profit)