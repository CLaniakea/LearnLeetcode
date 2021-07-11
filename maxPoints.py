from typing import List

class Solution:
    def is_same(self,slope1,slope2): # 判断斜率是否相同
        if slope1[1] == 0 and slope2[1] == 0 and slope2[0]!=0: #如果两个斜率均为正无穷（竖着的直线）并且第二个点不是第i个点
            return True
        elif slope1[1] == 0 or slope2[1] == 0:                 #如果有一个斜率为正无穷，那么直接返回False
            return False
        else:
            if slope1[0]/slope1[1] == slope2[0]/slope2[1]:     #斜率相同返回True
                return True
            else:
                return False

    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        if length == 1:
            return 1
        count_k = [[0]*length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                if i==j:
                    count_k[i][j]=[0,0]
                    count_k[j][i]=[0,0]
                    continue
                else:
                    count_k[i][j] = \
                        [points[i][1]-points[j][1], points[i][0]-points[j][0]]
                    count_k[j][i] = \
                        [points[i][1]-points[j][1], points[i][0]-points[j][0]]
        
                    
        count = 0
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                else:
                    flag = 1
                    for k in range(length):
                        if self.is_same(count_k[i][j],count_k[i][k]):
                            flag += 1
                    if flag > count:
                        count = flag
        return count


tag = Solution()
points = points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(tag.maxPoints(points))