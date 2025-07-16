cs=[] #철수
mc=[] #사회자
count = 0

for _ in range(5):
    a = list(map(int, input().split()))
    cs.append(a)

for _ in range(5):
    b = list(map(int, input().split()))
    mc.append(b)
    
def bingo():
    bingo_count = 0
    
    #가로줄 : 행
    for row in cs:
        if all(x == 'x' for x in row):
            bingo_count += 1
            
    #세로줄 : 열
    for col in range(5):
        if all(cs[row][col] == 'x' for row in range(5)):
            bingo_count += 1
    
    #대각선 \
    if all(cs[i][i] == 'x' for i in range(5)):
        bingo_count += 1
    
    #대각선 /
    if all(cs[i][4-i] == 'x' for i in range(5)):
        bingo_count += 1
    
    return bingo_count
##

for i in range(5):
    for j in range(5):
        count += 1
        
        for x in range(5):
            for y in range(5):
                if cs[x][y] == mc[i][j]:
                    cs[x][y] = 'x'
                    
        if bingo() >= 3:
            print(count)
            exit() #주피터에서 안 먹음
            #sys.exit()
