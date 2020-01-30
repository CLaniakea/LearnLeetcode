from typing import List
'''
最大子序和
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, maxSum = float("-inf"), float("-inf")
        for i in range(0, len(nums)):
            if maxSum > 0:
                maxSum += nums[i]
            else:
                maxSum = nums[i]
            if maxSum > sum:
                sum = maxSum
        return sum

tag = Solution()
nums = [-2, 1, -3, 4]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-1]
print(tag.maxSubArray(nums))

