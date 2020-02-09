from typing import List
'''
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
'''
''' before refer official answer'''
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False
        left = [0, 0]
        right = [row-1, col-1]
        while left[0] <= right[0]:
            #mid = [(left[0] + right[0])//2, ((((right[0]-left[0])*col + right[1] - left[1])//2) + left[1]) % col]
            mid = [left[0]+(((right[0] - left[0]) * col + right[1] - left[1]) // 2 + left[1])//col, ((((right[0] - left[0]) * col + right[1] - left[1]) // 2) + left[1]) % col]
            # $ ((right[0] - left[0])*col - left[1])%col
            # (((right[0] - 1 - left[0])*col - left[1] + right[1])//2)%col
            if matrix[mid[0]][mid[1]] == target:
                return True
            if left[0] == right[0] and left[1] > right[1]:
                return False
            elif matrix[mid[0]][mid[1]] > target:
                if mid[1] == 0:
                    mid[1] = col - 1
                    mid[0] = mid[0] - 1
                    right = mid
                    continue
                right = [mid[0], mid[1] - 1]
            else:
                if mid[1] == col - 1:
                    mid[1] = 0
                    mid[0] += 1
                    left = mid
                    continue
                left = [mid[0], mid[1] + 1]
        return False
'''
''' AFTER'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False
        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = (left + right) // 2
            r, c = mid // col, mid % col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
tag = Solution()
print(tag.searchMatrix([[1, 3]],2))
# print(-1%2)  1 2 3 4 5 6