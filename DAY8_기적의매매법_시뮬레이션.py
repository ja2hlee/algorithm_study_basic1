money = int(input())
stock_price = list(map(int, input().split()))

def jh():
    jh_money = money
    jh_stock = 0
    for i in range(14):
        if jh_money >= stock_price[i]:
            jh_stock += (jh_money // stock_price[i])
            jh_money %= stock_price[i]
        else:
            continue
    jh_final = jh_money + (stock_price[-1]*jh_stock)
    return jh_final    

def sm():
    sm_money = money
    sm_stock = 0
    for i in range(3, 14):
        if stock_price[i-3] > stock_price[i-2] > stock_price[i-1]: #연속하락
            if sm_money >= stock_price[i]:
                sm_stock += (sm_money // stock_price[i])
                sm_money %= stock_price[i]
        elif stock_price[i-3] < stock_price[i-2] < stock_price[i-1]: #연속상승
            sm_money += (sm_stock*stock_price[i])
            sm_stock = 0
    sm_final = sm_money + (stock_price[-1]*sm_stock)
    return sm_final

jh_final = jh()
sm_final = sm()

if jh_final > sm_final:
    print('BNP')
elif jh_final < sm_final:
    print('TIMING')
else:
    print('SAMESAME')



