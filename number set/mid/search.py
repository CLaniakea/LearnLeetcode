#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''-------------------'''
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,  7  ,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [7,0,1,  2  ,4,5,6], target = 3
'''
from typing import List

class Solution:
    def recursion(self, nums: List[int], left, right, target: int) -> int:
        mid = (right + left) // 2
        # 2 divide
        if nums[mid] > nums[right]:  # left order
            left1 = 0
            right1 = mid
            # nums1 = nums[:mid]
            while left1 <= right1:
                mid1 = (left1 + right1) // 2
                if nums[mid1] == target:
                    return mid1
                elif nums[mid1] > target:
                    right1 = mid1 - 1
                elif nums[mid1] < target:
                    left1 = mid1 + 1
            return self.recursion(nums, mid + 1, right, target)
        if nums[mid] < nums[right]:  # right order
            left2 = mid
            right2 = right
            while left2 <= right2:
                mid2 = (left2 + right2) // 2
                if nums[mid2] == target:
                    return mid2
                elif nums[mid2] > target:
                    right2 = mid2 - 1
                elif nums[mid2] < target:
                    left2 = mid2 + 1
            return self.recursion(nums, left, mid - 1, target)
        elif nums[mid] == target:
            return mid
        return -1
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.recursion(nums, 0, len(nums) - 1, target)

if __name__ == '__main__':
    tag = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = []
    target = 2
    print(tag.search(nums,target))