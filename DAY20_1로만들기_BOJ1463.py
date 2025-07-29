n = int(input())
dp = [0] * (n + 1) #최소 연산 횟수 저장하는 배열

for i in range(2, n + 1):
    #-1은 2나3의 나눗셈 조건에 해당하지 않아도 할 수 있어서 초기값
    dp[i] = dp[i - 1] + 1 #+1은 연산 횟수에 해당
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) 
        #위에서 실행한 dp[i - 1] + 1와 dp[i // 2] + 1중 더 작은 값을 저장
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])



