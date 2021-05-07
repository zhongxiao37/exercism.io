'''
Description: 
Author: Phoenix Zhong
Date: 2020-10-26 14:58:50
LastEditTime: 2020-11-11 17:26:03
LastEditors: Phoenix Zhong
FilePath: /python/new_coder_test.py
'''
def change(coins, target):
    memo = dict()
    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return [0]
        if n < 0:
            return None
        res = None
        for coin in coins:
            if n == coin:
                res = [coin]
            else:
                subproblem = dp(n - coin)
                if subproblem is None: continue
                if res is None or len(res) > len(subproblem):
                    res = subproblem + [coin]
        
        memo[n] = res
        return res
    return dp(target)


coins = [2, 5, 10, 11]
target = 20
print(change(coins, target))