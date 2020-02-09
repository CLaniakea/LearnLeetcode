from typing import List
'''

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for i in range(n)]
        for row in range(0, n):# 行
            for col in range(0, m):# 列
                if row > 0 and col > 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                else:
                    dp[row][col] = 1
        return dp[-1][-1]
        # for i in range(0,n):
        #     print(dp[i])
# [[1, 1], [1, 2], [1, 3]]
# 1 1 1
# 1 2 3

# 0 1 1
# 1 2 3
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
#         #print(dp)
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         print(dp)
#         return dp[-1][-1]
tag = Solution()
print(tag.uniquePaths(7,3))