from typing import List
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
             Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''
# class Solution:
#     def getMaxStep(self,nums: List[int], left, right, stp, tag):
#         maxValue = 0
#         for i in range(left, right):
#             if nums[i] + i >= len(nums) - 1:
#                 tag = 1
#                 stp += 1
#                 break
#             elif nums[i] >= maxValue:
#                 maxValue = nums[i]
#                 sub = i
#         return tag, stp, sub, maxValue
#     def jump(self, nums: List[int]) -> int:
#         right = len(nums) - 1
#         left = 0
#         step = 0
#         # tag = 0
#         while left < right:
#             if nums[left] + left >= right:
#                 step += 1
#                 break
#             else:
#                 step += 1
#                 tag, stp, sub, maxStep = self.getMaxStep(nums, left, left + nums[left] + 1, step, 0)
#                 # if stp - step != 1:
#                 #     return stp
#                 # step += 1
#                 if tag:
#                     print("stp")
#                     return stp
#                 else:
#                     if sub == left:
#                         left = left + nums[sub]
#                         # step += 1
#                     else:
#                         left = sub
#                         # step += 1
#         return step
'''
refer leetcode
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        step=0
        end=0
        max_bound=0
        for i in range(len(nums)-1):
            max_bound=max(max_bound,nums[i]+i)
            if(i==end):
                step+=1
                end=max_bound
        return step
tag = Solution()
# nums = [3,1,1,1,1]
# nums = [1,1,1,1,1]
# nums = [2,3,1,1,4]
# nums = [10,9,8,7,6,5,4,3,2,1,1,0]
# nums = [1, 2, 3, 4, 5]
# nums = [0]
# nums = [4,1,1,3,1,1,1]
nums = [9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]
print(tag.jump(nums))
