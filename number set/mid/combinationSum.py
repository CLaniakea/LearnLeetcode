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
#
#
# def permute(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ x + y
#                  for x in permute(1, s)
#                  for y in permute(list - 1, s)
#                 ]
#
#
#
#
# print(permute(1, ["a","b","c"]))
# print(permute(3, ["a","b","c"]))
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(combination, candidates, target, start):
            if not candidates:
                return
            # if combination and target < combination[-1]:
            #     return
            if target < 0:
                return
            if 0 == target:
                res.append(combination)
                return
            for i in range(start,len(candidates)):
                print("i", i, "start", start, "combination", combination)
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


