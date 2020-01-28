from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        i = 0
        res = float("inf")
        while i <= length - 3:
            L = i + 1
            R = length - 1
            while L != R and L < R:
                sum = nums[i] + nums[L] + nums[R]
                if abs(sum - target) < abs(res):
                    res = sum - target
                    reSum = sum
                '''
                The key point
                '''
                if sum > target:
                    R -= 1
                elif sum < target:
                    L += 1
                elif sum == target:
                    return sum
            while nums[i] == nums[i+1] and i+1 <= length - 3: i+=1
            i+=1
        return reSum

tag = Solution()
#nums = [-1, 2, 1, -4]
# nums = [1,1,1,0]
# target = -100
#target = 1
# nums = [0,2,1,-3]
# target = 1
nums = [1,2,5,10,11]
target = 12
print(tag.threeSumClosest(nums,target))