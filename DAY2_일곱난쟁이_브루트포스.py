dwarps = []

for i in range(9):
    height = int(input())
    dwarps.append(height)
    
dwarps.sort()
dwarp1,dwarp2 = 0, 0
fake_dwarp = sum(dwarps)-100

for i in range(len(dwarps)-1):
    for j in range(i+1,len(dwarps)):
        if dwarps[i]+dwarps[j]==fake_dwarp:
            dwarp1,dwarp2 = dwarps[i], dwarps[j]
            break
            
dwarps.remove(dwarp1)
dwarps.remove(dwarp2)

#오름차순으로 출력
for k in dwarps:
    print(k)