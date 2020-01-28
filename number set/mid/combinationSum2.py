from typing import List
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    def backtrack(self, start, candidates, target, combination, res):
        i = start
        # print("res =", res)
        while start <= i < len(candidates):
            if candidates[i] > target:
                return
            elif candidates[i] == target:
                res.append(combination + [candidates[i]])
                return
            else:
                self.backtrack(i + 1, candidates, target - candidates[i], combination + [candidates[i]], res)
                while i < len(candidates) - 1 and candidates[i + 1] == candidates[i] : i += 1
                i += 1
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        candidates.sort()
        self.backtrack(start = 0, candidates = candidates, target = target, combination = [], res = res)
        return res

if __name__ == "__main__":
    tag = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    # candidates = [2, 5, 2, 1, 2]
    # target = 5
    print(tag.combinationSum2(candidates, target))

