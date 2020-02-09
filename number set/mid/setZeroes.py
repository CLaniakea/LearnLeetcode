from typing import List
'''
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lable = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    lable.append([i,j])
        for r,c in lable:
            for i in range(row):
                matrix[i][c] = 0
            for j in range(col):
                matrix[r][j] = 0

        print(matrix)


tag = Solution()
L = [[1,1,1],
     [1,0,1],
     [1,1,1]]
M = [[0,1,2,0],
     [3,4,5,2],
     [1,3,1,5]
]
print(tag.setZeroes(M))