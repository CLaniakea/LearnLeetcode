from typing import List
'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''
'''
如果nums[i],nums[i+1],nums[i+2]
'''
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return len(nums)
#         count = 0
#         l = 0
#         r = 1
#         while r < len(nums):
#             if nums[l] != nums[r]:
#                 count += 1
#                 l = r
#                 r = l + 1
#             else:
#                 while r < len(nums) and nums[r] == nums[r - 1]:
#                     r += 1
#                 nums = nums[:l + 2] + nums[r:]
#                 l = l + 2
#                 r = l + 1
#                 count += 2
#                 if r >= len(nums) and l < len(nums):
#                     count += 1
#         # print(nums)
#         return count

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for e in nums:
            if i < 2 or e != nums[i - 2]:
                nums[i] = e
                i += 1
        return i

# nums = [0,0,1,1,1,1,2,3]
# nums = [1,1,1,2,2,3]
nums = [1,1,1,2,2,3]
tag = Solution()
print(tag.removeDuplicates(nums))