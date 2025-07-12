n, m = map(int, input().split())
square = [input() for _ in range(n)]

square_s = 1  #넓이가 1인 경우도 생각해야함

for i in range(n):
    for j in range(m):
        k = 1
        while i+k<n and j+k<m:
            if square[i][j] == square[i+k][j] == square[i][j+k] == square[i+k][j+k]:
                square_s = max(square_s, (k+1)**2)
            k+=1

print(square_s)