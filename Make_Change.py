#
#  Make Change Program - make change in Quarters, Dimes, Nickels and Pennys
# 
import math
def min_coins(cents):
    if cents < 1:
        return 0
    coins = [25 ,10, 5, 1]  # Quarters, Dimes, Nickels, Pennys
    
    number_of_coins = 0
    value_in_coins = []
    qtrCnt = 0  
    dimeCnt = 0 
    nickelCnt = 0
    pennyCnt = 0
    for coin in coins:
        number_of_coins += math.floor(cents/coin)
        while cents >= coin:
            value_in_coins.append(coin)
            cents -= coin
        cents = cents % coin
        if cents == 0:
            break  
    for v in value_in_coins:    #### Loop the list to increment varibles for the amount of Qtr's Dimes Nickels & Pennys
        if v == 25:
            qtrCnt += 1
        elif v == 10:
            dimeCnt += 1
        elif v == 5:
            nickelCnt += 1
        elif v == 1:
            pennyCnt += 1
    text = "{v1}-Quarters {v2}-Dimes {v3}-Nickels {v4}-Pennys ".format(v1=qtrCnt,v2=dimeCnt,v3=nickelCnt,v4=pennyCnt)
    print(value_in_coins)
    print(text)
    return number_of_coins

print(min_coins(59)," Coins\n")


