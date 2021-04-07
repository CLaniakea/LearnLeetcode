from typing import List
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much 
water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
# before optimization
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0
        left = 0
        right = 1
        volume = 0
        while left < length - 1 and right < length:
            if height[left] == 0:
                left += 1
                right += 1
                continue
            elif height[left] > height[right]:
                if right == length - 1 and left != right - 1:
                    height[left] -= 1
                    right = left + 1
                    continue
                right += 1
            elif height[left] <= height[right]:
                v = 0
                for i in range(left + 1, right):
                    v += height[i]
                volume += height[left] * (right-left-1) - v
                left = right
                right += 1
        return volume
'''
# after optimization


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        volume = 0
        leftMax = rightMax = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    volume += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    volume += rightMax - height[right]
                right -= 1
        return volume


tag = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [5,4,1,2]
# height = [2,0,2]
# height = [4,3,5,3,4]
print(tag.trap(height))
