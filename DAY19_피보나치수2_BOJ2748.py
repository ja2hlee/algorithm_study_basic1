fn = [0,1]
n = int(input())

for i in range(2,n+1):
    fn.append(fn[i-1]+fn[i-2])
print(fn[n])

