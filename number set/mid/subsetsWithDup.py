from typing import List
'''
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def helper(i, tmp):
            if tmp not in res:
                res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

L = [1, 2, 2]
L = [4,4,4,1,4]
tag = Solution()
print(tag.subsetsWithDup(L))