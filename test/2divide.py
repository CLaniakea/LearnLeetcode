from typing import List
def divide_search(nums: List[int], target:int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right)/2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1

def recursion_2_search(nums:List[int], target:int):
    left = 0
    right = len(nums) - 1
    mid = int((left + right)/2)
    if not nums:
        return -1
    elif nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return recursion_2_search(nums[:mid], target)
    elif nums[mid] < target:
        return recursion_2_search(nums[mid + 1:], target)

def binary_search(lis, left, right, num):

    if left > right:  # 递归结束条件
        return -1
    mid = (left + right) // 2
    if num < lis[mid]:
        right = mid - 1
    elif num > lis[mid]:
        left = mid + 1
    else:
        return mid
    return binary_search(lis, left, right, num)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
print(divide_search(nums, target))
print(recursion_2_search(nums, target))
print(binary_search(nums, 0, 8, target))