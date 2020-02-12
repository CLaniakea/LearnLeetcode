from typing import List
'''
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
'''
'''
参考
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == [] or board == [[]]:
            return False
        row = len(board)
        col = len(board[0])
        dic = [(0, 1), (0, -1), (1, 0), (-1, 0)]# 右， 下， 左， 上
        mark = [[0 for _ in range(col)] for _ in range(row)]

        def helper(i, j, word, mark):
            if len(word) == 0:
                return True
            for d in dic:
                new_row = i + d[0]
                new_col = j + d[1]
                if new_col >= 0 and new_col < col and new_row >= 0 and new_row < row and board[new_row][new_col] == word[0]:
                    if mark[new_row][new_col] == 1:
                        continue
                    mark[new_row][new_col] = 1
                    if helper(new_row, new_col, word[1:], mark) == True:
                        return True
                    else:
                        mark[new_row][new_col] = 0
            return False

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    mark[r][c] = 1
                    if helper(r, c, word[1:], mark) == True:
                        return True
                    else: mark[r][c] = 0
        return False

# class Solution(object):
#     # 定义上下左右四个行走方向
#     directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         m = len(board)
#         if m == 0:
#             return False
#         n = len(board[0])
#         mark = [[0 for _ in range(n)] for _ in range(m)]
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     # 将该元素标记为已使用
#                     mark[i][j] = 1
#                     if self.backtrack(i, j, mark, board, word[1:]) == True:
#                         return True
#                     else:
#                         # 回溯
#                         mark[i][j] = 0
#         return False
#
#     def backtrack(self, i, j, mark, board, word):
#         if len(word) == 0:
#             return True
#
#         for direct in self.directs:
#             cur_i = i + direct[0]
#             cur_j = j + direct[1]
#
#             if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == \
#                     word[0]:
#                 # 如果是已经使用过的元素，忽略
#                 if mark[cur_i][cur_j] == 1:
#                     continue
#                 # 将该元素标记为已使用
#                 mark[cur_i][cur_j] = 1
#                 if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
#                     return True
#                 else:
#                     # 回溯
#                     mark[cur_i][cur_j] = 0
#         return False



# board =[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
board = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]
]
word = "AAB"
# word = "CFD"
tag = Solution()
print(tag.exist(board, word))