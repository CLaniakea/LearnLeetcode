from typing import List
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tagLeft = -1
        tagRight = -1
        if not nums:
            return [tagLeft, tagRight]
        if nums[0] > target or nums[-1] < target:
            return [tagLeft, tagRight]
        right, length = len(nums) - 1, len(nums) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                tagMid = mid
                while mid - 1 >= 0 and nums[mid - 1] == target: mid -= 1
                tagLeft = mid
                mid = tagMid
                while mid + 1 <= length and nums[mid + 1] == target: mid += 1
                tagRight = mid
                break
        return [tagLeft, tagRight]

'''test example'''
if __name__ == "__main__":
    tag = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    target = 1
    nums = [1]
    print(tag.searchRange(nums, target))
'''
执行结果：通过
显示详情执行用时 : 100 ms, 在所有 Python3 提交中击败了73.47%的用户
内存消耗 : 14.6 MB, 在所有 Python3 提交中击败了55.37%的用户
'''