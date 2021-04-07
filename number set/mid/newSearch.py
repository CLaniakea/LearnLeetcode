# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:17:14 2021

@author: 15866
"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return False
        left = 0
        length = len(nums)
        right = length - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -=1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[length - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    tag = Solution()
    # nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    # nums = []
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    print(tag.search(nums,target))