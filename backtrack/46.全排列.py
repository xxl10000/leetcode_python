#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start

# 用visited数组判断该元素是否已经访问过，而不是直接用nums[i] not in nums这样O(n)的方法

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        onpath = []
        visited = [False] * len(nums)
        def backtrack():
            if len(onpath) == len(nums):
                res.append(onpath[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    onpath.append(nums[i])
                    backtrack()
                    onpath.pop()
                    visited[i] = False
            
        backtrack()
        return res

# 用递归去理解，f(n) 怎么从f(n - 1) 状态得来。   
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def backtrack(idx):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                swap(idx, i)
                backtrack(idx + 1)
                swap(idx, i)
        backtrack(0)
        return res
# @lc code=end

