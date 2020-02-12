from typing import List
'''
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
'''
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # ERROR ERROR ERROR
#         left = 0
#         right = len(nums) - 1
#         for mid in range(len(nums)):
#             if mid <= right:
#                 if nums[mid] == 0:
#                     nums[mid], nums[left] = nums[left], nums[mid]
#                     left += 1
#                 elif nums[mid] == 2:
#                     nums[mid], nums[right] = nums[right], nums[mid]
#                     right -= 1
#         print(nums)

# COPY COPY COPY
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums)-1
        middle = 0
        first = 0
        while middle <= last:
            if nums[middle] == 2:
                nums[middle], nums[last] = nums[last], nums[middle]
                last -= 1
            elif nums[middle] == 0:
                nums[first] = 0
                if middle > first:
                    nums[middle] = 1
                first += 1
                middle += 1
            else:
                middle += 1
tag = Solution()
nums = [2,0,2,1,1,0]
# nums = [2,2,0,0,1,1]
# nums = [2,0,1]
nums = [1,2,0]
print(tag.sortColors(nums))