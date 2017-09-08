# Count the number of ways we can make change. For each denomination (going from high to low), we use every possible number of coins of that denomination and recursively try the smaller denominations.

coins = [50,25,10,5,1]

def solve(rem, denom):
    if rem < 0:
        assert(False)
        return 0
    elif rem == 0:
        return 1
    elif denom == len(coins) - 1:
        return 1
    else:
        max_num_coin = rem // coins[denom]
        num_ways = 0
        for num_coin in range(max_num_coin + 1):
            num_ways += solve(rem - num_coin * coins[denom], denom+1)
    return num_ways
        


print(solve(100,0))
assert(solve(5,3) == 2)
assert(solve(10,3) == 3)
assert(solve(10,2) == 4)
