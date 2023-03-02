#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, onpath = [], []
        thisSum = 0
        candidates.sort()
        def backtrack(start):
            nonlocal thisSum
            if thisSum == target:
                res.append(onpath[:])
                return
            if thisSum > target:
                return  
            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                thisSum += candidates[i]
                onpath.append(candidates[i])
                backtrack(i + 1)
                onpath.pop()
                thisSum -= candidates[i]
        backtrack(0)
        return res
        
# @lc code=end

