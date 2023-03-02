#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
# for in 和 backtrack里面变量是根据题意如何回溯决定的。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, onpath = [], []
        def backtrack(start):
            res.append(onpath[:])
            for i in range(start, len(nums)):
                onpath.append(nums[i])
                backtrack(i + 1)
                onpath.pop()
        backtrack(0)
        return res
# @lc code=end

