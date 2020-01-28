# a good example
from typing import List
'''
class Solution:
    def get2nums(self, nums: List[int]) -> List[List[int]]:
        j = len(nums) - 1
        i = 0
        L, temp = [], []
        while i < j - 1:
            k = 0
            while k <= j:
                if i != k:
                    temp.append(nums[i])
                    temp.append(nums[k])
                    L.append(temp)
                    temp = []
                k += 1
            i += 1
        return L
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        j = len(nums) - 1
        L = self.get2nums(nums)
        length = len(L)
        res = []
        target = 0
        temp = []
        while target < length:
            i = 0
            while i <= j:
                if L[target][0] + L[target][1] + nums[i] == 0:
                    temp = [L[target][0], L[target][1], nums[i]]
                    res.append(temp)
                    temp = []
                i += 1
            target += 1
        return res
'''
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        i = 0
        res = []
        break_tag = False
        while i <= length -3:
            j = i + 1
            while j <= length - 2:
                k = j + 1
                while k <= length - 1:
                    if nums[i] > 0:
                        break_tag = True
                        break
                    elif nums[k] < 0:
                        k += 1
                        continue
                    elif nums[i]+nums[j]+nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                    k += 1
                if break_tag:
                    break
                else: j += 1
            if break_tag:
                break
            else: i += 1
        res = list(set(tuple(t) for t in res))
        res = [list(t) for t in res]
        return res
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        i = 0
        res = []
        while i <= length - 3:
            L = i + 1
            R = length - 1
            if nums[i] > 0:
                break
            while L != R and L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while nums[L + 1] == nums[L] and L+1 < R: L += 1
                    L += 1
                    while nums[R - 1] == nums[R] and R-1 > i: R -= 1
                    R -= 1
                elif sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
            while nums[i] == nums[i+1] and i+1 <= length - 3: i+=1
            i+=1
        return res
tag = Solution()
# nums = [-7,-1,-13,2,13,2,12,3,-11,3,7,-15,2,-9,-13,-13,11,-10,5,-13,2,-12,0,-8,8,-1,4,10,-13,-5,-6,-4,9,-12,5,8,5,3,-4,9,13,10,10,-8,-14,4,-6,5,10,-15,-1,-3,10,-15,-4,3,-1,-15,-10,-6,-13,-9,5,11,-6,-13,-4,14,-3,8,1,-4,-5,-12,3,-11,7,13,9,2,13,-7,6,0,-15,-13,-11,-8,9,-14,1,11,-7,13,0,-6,-15,11,-6,-2,4,2,9,-15,5,-11,-11,-11,-13,5,7,7,5,-10,-7,6,-7,-11,13,9,-10,-9]
#nums = [-4, -1, -1, 0, 1, 2]
# nums = [1,2,-2,-1]
#nums = [2,-8,8,6,-14,-12,11,-10,13,14,7,3,10,-13,3,-15,7,3,-11,-8,4,5,9,11,7,1,3,13,14,-13,3,-6,-6,-12,-15,-12,-9,3,-15,-11,-6,-1,0,11,2,-12,3,-6,6,0,-6,-12,-10,-12,6,5,-4,-5,-5,-4,-11,13,5,-2,-13,-3,-7,-15,8,-15,12,-13,0,-3,6,9,-8,-6,10,5,9,-11,0,7,-15,-8,-3,-4,-6,7,7,-2,-2,-11,3,0,-6,12,0,-13,4,-3,11,-11,1,2,13,8,4,9,-1,-2,5,14,12,5,13,-6,-13,-8,9,1,5,-8,-2,-6,-1]
#nums = [-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3]
#nums = [-2,0,0,2,2]
nums = [1,2,3,4]
L = tag.threeSum(nums)
print(L)
