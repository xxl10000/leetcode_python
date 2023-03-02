#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
# 思考如何剪枝，也就是在选择列表里面去掉不合适的选择
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, onpath = [], []
        nums.sort()
        def backtrack(start):
            res.append(onpath[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:  # i > start not i > 0
                    continue
                onpath.append(nums[i])
                backtrack(i + 1)
                onpath.pop()
        backtrack(0)
        return res
# @lc code=end

