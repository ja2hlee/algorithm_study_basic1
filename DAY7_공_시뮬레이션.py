m = int(input())
    
ball =[1, 0, 0]

for _ in range(m):
    a, b = map(int, input().split())
    tmp = ball[a-1]
    ball[a-1] = ball[b-1]
    ball[b-1]=tmp

print(ball.index(1)+1)