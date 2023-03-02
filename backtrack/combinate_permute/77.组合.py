#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
# 思路同78，也就是终止条件不同
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, onpath = [], []
        def backtrack(start):
            if len(onpath) == k:
                res.append(onpath[:])
                return 
            for i in range(start, n + 1):
                onpath.append(i)
                backtrack(i + 1)
                onpath.pop()
        backtrack(1)
        return res
# @lc code=end

