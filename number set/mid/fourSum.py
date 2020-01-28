from typing import List
# I
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        if nums[-1] * 4 < target:
            return []
        length = len(nums)
        i = 0
        res = []
        while i <= length - 4:
            if nums[i] * 4 > target:
                break
            j = length - 1
            while j >= 3:
                if nums[j] * 4 < target:
                    break
                L = i + 1
                R = j - 1
                while L < R:
                    sum = nums[i] + nums[j] + nums[L] + nums[R]
                    if sum == target:
                        res.append([nums[i], nums[L], nums[R], nums[j]])
                        while nums[L + 1] == nums[L] and L + 1 < R: L += 1
                        L += 1
                        while nums[R - 1] == nums[R] and R - 1 > i: R -= 1
                        R -= 1
                    elif sum > target:
                        R -= 1
                    elif sum < target:
                        L += 1
                while nums[j] == nums[j - 1] and j >= 3: j -= 1
                j -= 1
            while nums[i] == nums[i + 1] and i <= length - 4: i += 1
            i += 1
        return res
'''
# da lao
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
 
        if not nums:
            return []
        
        _4_sum_list = []
        nums.sort()
        if nums[-1]*4 < target:
            return []
        for i in range(len(nums)-3):
            if nums[i]*4 > target:
                break
            if i==0 or nums[i]!= nums[i-1]:
                ele = nums[i]
                target_3_sum = target - ele
                if nums[-1]*3 < target_3_sum:
                    continue
                for j in range(i+1,len(nums)-2):
                    ele2 = nums[j]
                    if ele2*3 > target_3_sum:
                        break
                    if j==i+1 or ele2!= nums[j-1]:
                        target_2_sum = target_3_sum - ele2
                        point_left = j+1
                        point_right = len(nums)-1
                        while point_left < point_right:
                            if nums[point_left] + nums[point_right] > target_2_sum:
                                point_right -= 1
                            elif nums[point_left] + nums[point_right] < target_2_sum:
                                point_left += 1
                            else:
                                aaa = [ele, ele2,nums[point_left], nums[point_right]]
                                _4_sum_list.append(aaa)
                                point_left += 1
                                point_right -= 1
                                while point_left < point_right and nums[point_left] == nums[point_left-1]:
                                    point_left += 1
                                while point_left < point_right and nums[point_right] == nums[point_right+1]:
                                    point_right -= 1
 
 
        return _4_sum_list
'''
ex = Solution()
# nums = [1, 0, -1, 0, -2, 2]
#nums = [0,0,0,0]
#nums = [-3,-2,-1,0,0,1,2,3]
nums = [-5,5,4,-3,0,0,4,-2]
target = 4
print(ex.fourSum(nums,target))
#[-3,0,1,2],[-2,-1,0,3]