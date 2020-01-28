from typing import List
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
# class Solution:
#     def judge(self, n):
#         if True:
#             return True
#         return False
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         pass
# def permute(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ x + y
#                  for x in permute(1, s)
#                  for y in permute(list - 1, s)
#                 ]
# print(permute(1, ["a","b","c"]))
# print(permute(3, ["a","b","c"]))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(combination, candidates, target, start):# no start will generate repeated answers
            if not candidates:
                return
            # if combination and target < combination[-1]:
            #     return
            if target < 0:
                #print("target", target, "combination", combination)
                return
            if 0 == target:
                #print("target = 0 combination", combination)# test
                res.append(combination)
                return
            for i in range(start,len(candidates)):
                #print("i", i, "start", start, "combination", combination)# test
                #print("combination + [candidates[i]]", combination + [candidates[i]], "candidates", candidates, "target - candidates[i]", target - candidates[i], "i", i)
                if candidates[i] <= target:
                    backtrack(combination + [candidates[i]], candidates, target - candidates[i], i)
        backtrack([], candidates, target, 0)
        return res

'''
class Solve:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = list()
        candidates.sort()
        self._combinationSum(candidates, target, 0, list(), result)
        return result

    def _combinationSum(self, nums, target, index, path, res):
        if target < 0:
            return

        if target == 0:
        # if len(path) == 5:
            res.append(path)
            return

        for i in range(index, len(nums)):
            self._combinationSum(nums, target - nums[i], i, path + [nums[i]], res)

'''
if __name__ == '__main__':
    #nums = [1, 2, 3]
    nums = [2, 3, 6, 7]
    target = 10
    solution = Solution()
    #solve = Solve()
    print(solution.combinationSum(nums,target))
    #print(solve.combinationSum(nums,target))
'''
i 0 start 0 combination []
i 0 start 0 combination [2]
i 0 start 0 combination [2, 2]
i 0 start 0 combination [2, 2, 2]
i 0 start 0 combination [2, 2, 2, 2]
target = 0 combination [2, 2, 2, 2, 2]


i 1 start 0 combination [2, 2, 2, 2]
target -1 combination [2, 2, 2, 2, 3]

i 2 start 0 combination [2, 2, 2, 2]
target -4 combination [2, 2, 2, 2, 6]

i 3 start 0 combination [2, 2, 2, 2]
target -5 combination [2, 2, 2, 2, 7]


i 1 start 0 combination [2, 2, 2]
i 1 start 1 combination [2, 2, 2, 3]
target -2 combination [2, 2, 2, 3, 3]

i 2 start 1 combination [2, 2, 2, 3]
target -5 combination [2, 2, 2, 3, 6]

i 3 start 1 combination [2, 2, 2, 3]
target -6 combination [2, 2, 2, 3, 7]


i 2 start 0 combination [2, 2, 2]
target -2 combination [2, 2, 2, 6]

i 3 start 0 combination [2, 2, 2]
target -3 combination [2, 2, 2, 7]


i 1 start 0 combination [2, 2]
i 1 start 1 combination [2, 2, 3]
target = 0 combination [2, 2, 3, 3]

i 2 start 1 combination [2, 2, 3]
target -3 combination [2, 2, 3, 6]

i 3 start 1 combination [2, 2, 3]
target -4 combination [2, 2, 3, 7]


i 2 start 0 combination [2, 2]
target = 0 combination [2, 2, 6]

i 3 start 0 combination [2, 2]
target -1 combination [2, 2, 7]


i 1 start 0 combination [2]
i 1 start 1 combination [2, 3]
i 1 start 1 combination [2, 3, 3]
target -1 combination [2, 3, 3, 3]

i 2 start 1 combination [2, 3, 3]
target -4 combination [2, 3, 3, 6]

i 3 start 1 combination [2, 3, 3]
target -5 combination [2, 3, 3, 7]

i 2 start 1 combination [2, 3]
target -1 combination [2, 3, 6]

i 3 start 1 combination [2, 3]
target -2 combination [2, 3, 7]


i 2 start 0 combination [2]
i 2 start 2 combination [2, 6]
target -4 combination [2, 6, 6]

i 3 start 2 combination [2, 6]
target -5 combination [2, 6, 7]


i 3 start 0 combination [2]
i 3 start 3 combination [2, 7]
target -6 combination [2, 7, 7]


i 1 start 0 combination []
i 1 start 1 combination [3]
i 1 start 1 combination [3, 3]
i 1 start 1 combination [3, 3, 3]
target -2 combination [3, 3, 3, 3]

i 2 start 1 combination [3, 3, 3]
target -5 combination [3, 3, 3, 6]

i 3 start 1 combination [3, 3, 3]
target -6 combination [3, 3, 3, 7]


i 2 start 1 combination [3, 3]
target -2 combination [3, 3, 6]

i 3 start 1 combination [3, 3]
target -3 combination [3, 3, 7]


i 2 start 1 combination [3]
i 2 start 2 combination [3, 6]
target -5 combination [3, 6, 6]

i 3 start 2 combination [3, 6]
target -6 combination [3, 6, 7]


i 3 start 1 combination [3]
target = 0 combination [3, 7]
i 2 start 0 combination []
i 2 start 2 combination [6]
target -2 combination [6, 6]
i 3 start 2 combination [6]
target -3 combination [6, 7]
i 3 start 0 combination []
i 3 start 3 combination [7]
target -4 combination [7, 7]
'''
