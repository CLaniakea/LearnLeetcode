from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        elif nums[0] < nums[-1]:
            return nums[0]
        else:
            left = 0
            right = len(nums) - 1
            while(left < (right-1)):
                mid = (left + right) // 2
                if nums[mid] < nums[right]:
                    right = mid
                elif nums[mid] > nums[right]:
                    left = mid
                else:
                    right -= 1
            return min(nums[left], nums[right])


tag = Solution()
nums = [3,3,1,3]
print(tag.findMin(nums))