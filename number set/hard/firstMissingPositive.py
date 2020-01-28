from typing import List
'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''
# can be optimized
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        nums.sort()
        if nums[-1] < 1:
            return 1
        target=1
        for i in range(0,len(nums)):
            if nums[i] == target:
                target += 1
                continue
            elif nums[i] < target:
                continue
            else:
                break
        return target

'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visit = [-1]*(len(nums))
        for i in range(0, len(nums)):
            if nums[i] != i + 1 and nums[i] <= len(nums):
                tmp = nums[i]
                nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]
                visit[tmp - 1] = 1
                #nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        i = 0
        while i <len(nums) and nums[i] == i + 1: i += 1
        return i + 1
'''
tag = Solution()
# nums = [1,2,0]
# nums=[7,8,9,11,12]
nums=[3,4,-1,1]
print(tag.firstMissingPositive(nums))