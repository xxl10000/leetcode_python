#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, onpath = [], []
        pathSum = 0
        
        def backtrack(start):
            nonlocal pathSum
            if pathSum > n:
                return
            if len(onpath) == k:
                if pathSum == n:
                    res.append(onpath[:])
                return
            for i in range(start, 10):
                onpath.append(i)
                pathSum += i
                backtrack(i + 1)
                pathSum -= i
                onpath.pop()
                
        backtrack(1)
        return res
# @lc code=end

