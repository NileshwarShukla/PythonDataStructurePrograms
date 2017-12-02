def min_Coins(target,coins,known_tar):
    minCoins=target
    if target in coins:
        known_tar[target]=1
    if known_tar[target]>0:
        return known_tar[target]
    for i in [c for c in coins if c<=target]:
        numcoins=1+min_Coins(target-i,coins,known_tar)
        if numcoins<minCoins:
            minCoins=numcoins
            known_tar[target]=minCoins
    return known_tar[target]

target=14
coins=[1,2,5]
coin_arr=[0]*(target+1)
print min_Coins(target,coins,coin_arr)
