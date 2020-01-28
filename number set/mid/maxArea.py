from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        i = 0
        j = length - 1
        area = j * min(height[i],height[j])
        while j - 1 != i:
            maxHeight = max(height[i],height[j])
            if height[i] == maxHeight:
                j -= 1
            else:
                i += 1
            areaCache = (j - i) * min(height[i], height[j])
            area = max(area,areaCache)
        return area


tag = Solution()
L = [1, 1]
print(tag.maxArea(L))