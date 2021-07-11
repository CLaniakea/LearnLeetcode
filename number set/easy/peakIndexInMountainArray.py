from typing import List
# O(n)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        for i in range(length-1):
            if arr[i] < arr[i+1]:
                continue
            else:
                return i

arr = [24,69,100,99,79,78,67,36,26,19]
tag = Solution()
print(tag.peakIndexInMountainArray(arr))


# O(log(N))
class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        left, right = 0, length - 1
        while(True):
            mid = (left + right) // 2
            if (arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]):
                right = mid - 1
            elif(arr[mid] < arr[mid + 1] and arr[mid] > arr[mid - 1]):
                left = mid + 1
            else:
                return mid


arr = [24,69,100,99,79,78,67,36,26,19]
tag = Solution1()
print(tag.peakIndexInMountainArray(arr))