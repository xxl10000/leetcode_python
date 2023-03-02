#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
# if 语句后面如果太多，用continue
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, onpath = [], []
        visited = [False] * len(nums)
        def backtrack():
            if len(onpath) == len(nums):
                res.append(onpath[:])
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                onpath.append(nums[i])
                backtrack()
                onpath.pop()
                visited[i] = False
        backtrack()
        return res
# @lc code=end

