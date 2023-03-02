#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
# 去除去重逻辑， backtrack(i + 1) -> backtrack(i) 即可
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, onpath = [], []
        pathSum = 0
        def backtrack(start):
            nonlocal pathSum
            if pathSum > target:
                return
            if pathSum == target:
                res.append(onpath[:])
                return
            
            for i in range(start, len(candidates)):
                onpath.append(candidates[i])
                pathSum += candidates[i]
                backtrack(i)
                pathSum -= candidates[i]
                onpath.pop()
        backtrack(0)
        return res
# @lc code=end

obj = Solution()
res = obj.combinationSum(list(range(1,7)), 6)
for v in res:
    print(v)

