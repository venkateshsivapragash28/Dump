coins = [1,2,5]
coins = coins[::-1]
count = 0
sum = 23
def coins_count(coins, sum, count):
    for coin in coins:
        while sum >= coin:
            sum = sum - coin
            count = count + 1
    if sum == 0:
        return count
    return -1

print(coins_count(coins, sum ,count))
