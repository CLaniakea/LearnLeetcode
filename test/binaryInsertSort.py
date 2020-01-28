from typing import List
class Solution:
    def binaryInsertSort(self, nums: List) -> List:
        length = len(nums)
        i = 2
        while i < length:
            left = 1
            right = i - 1
            nums[0] = nums[i]
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[0]:
                    right = mid - 1
                # elif nums[mid] < nums[0]:
                #     left = mid + 1
                else:
                    left = mid + 1
                    # [_5_, 1, 3, 4, 5]
                    # left move ......
                # elif nums[mid] == nums[0]:
                #     i += 1
                #     break
            j = i - 1
            while j >= left:
                nums[j + 1] = nums[j]
                j -= 1
            nums[left] = nums[0]
            i += 1
        return nums


tag = Solution()
print(tag.binaryInsertSort([0, 5, 5, 5, 2, 7, 9, 6, 8, 4]))