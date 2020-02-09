from typing import List
'''

'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,row):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
        for j in range(1,col):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j - 1]
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = 0
        # print(obstacleGrid)
        return obstacleGrid[-1][-1]


        # dp = dp = [[0] * col for i in range(row)]
        # for r in range(0, row):# 行
        #     for c in range(0, col):# 列
        #         if r > 0 and c > 0:
        #             if obstacleGrid[r][c] == 0:
        #                 dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        #             else:
        #                 dp[r][c] = 0
        #         else:
        #             if obstacleGrid[r][c] == 0:
        #                 dp[r][c] = 1
        #             else:
        #                 if r == c and r == 0:
        #                     return 0
        #                 dp[r][c] = 0
        # return dp[-1][-1]
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.
        print(obstacleGrid)
        return obstacleGrid[m-1][n-1]
'''


# 1 1 1
# 1 1 0
# 1 0 0
L = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
M = [[1,0]]
N = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
]
X = [[0, 0]]
Y = [[0,0],[1,1],[0,0]]
tag = Solution()
print(tag.uniquePathsWithObstacles(Y))