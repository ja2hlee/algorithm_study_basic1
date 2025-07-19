n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)

def dfs(index, result, add, sub, mul, div):
    global max_result, min_result
    if index == n: #수를 다 사용했을 때 멈추도록
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if add>0:
        #dfs(다음 번호, 남은 덧셈 연산자있으면 계산, 사용한 연산자 개수 줄임, ...)
        dfs(index+1, result+nums[index], add-1, sub, mul, div)
    if sub>0:
        dfs(index+1, result-nums[index], add, sub-1, mul, div)
    if mul>0:
        dfs(index+1, result*nums[index], add, sub, mul-1, div)
    if div>0:
        if result < 0:
            dfs(index+1, -(-result//nums[index]), add, sub, mul, div-1)
        else:
            dfs(index+1, result//nums[index], add, sub, mul, div-1)
            
#연산자 끼워넣기 시작하는 index,숫자시작, ...
dfs(1, nums[0], add, sub, mul, div)

print(max_result)
print(min_result)