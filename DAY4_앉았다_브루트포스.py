from itertools import combinations

def jokbo(a, b):
    if a == b:
        return 50+a 
    else:
        return (a+b)%10
    
a, b = map(int, input().split())

cards = []
for i in range(1, 11):
    cards += [i, i]

#영학이 카드 제거
cards.remove(a)
cards.remove(b)

win, total = 0, 0
for i, j in combinations(cards, 2):
    mine = jokbo(a, b)
    others = jokbo(i, j)
    if mine > others:
        win += 1
    total += 1

        
print(f"{win / total:.3f}")
