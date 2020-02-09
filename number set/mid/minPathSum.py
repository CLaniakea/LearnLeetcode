from typing import List
'''
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
minSum[i][j] = min(minSum[i][j-1], minSum[i-1][j]) + grid[i][j]
another:
stack  
    visit 1, push 3, visit 1, push 5, visit 4, no below, visit 2,no below, visit 1, get sum1 -> minSum = sum1
                                    , visit 2, push 1, visit 1
                                                     , visit 1
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # the first row
        for i in range(1,row):
            grid[i][0] += grid[i-1][0]
        for j in range(1,col):
            grid[0][j] += grid[0][j-1]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
        # print(grid)
        return grid[-1][-1]

tag = Solution()
L = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
output = [
    [1, 4, 5],
    [2, 7, 6],
    [6, 8, 7]
]
print(tag.minPathSum(L))
