"""
给定 k 种面值的硬币, c_1...k,
总金额 amount，求最少几枚硬币
"""

from typing import List
### 暴力递归
class Coins:
    def coinsChange(self, coins:List, amount:int):
        def dp(n):
            if n == 0 :
                return 0
            if n <= 0:
                return -1
            
            res = float('INF')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            return res if res != float('INF') else -1
            # print(n)
        return dp(amount)

### 添加备忘录
### 自顶向下
class CoinsMemo:
    def coinsChange(self, coins:List, amount:int):
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]

            if n == 0 :
                return 0
            if n <= 0:
                return -1
            
            res = float('INF')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            memo[n] = res if res != float('INF') else -1
            # print(n)

            return memo[n]
        return dp(amount)

### dp table
### 自底向上
class CoinsTable:
    def coinsChange(self, coins:List, amount:int):
        table = [_ + 1 for _ in range(amount + 1)]
        table[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                table[i] = min(table[i], 1 + table[i - coin])
        
        return table[amount] if table[amount] != amount+1 else -1


coins = [1, 2, 3]
amount = 110
# tag = Coins()
tag = CoinsMemo()
# tag = CoinsTable()

print(tag.coinsChange(coins, amount))
