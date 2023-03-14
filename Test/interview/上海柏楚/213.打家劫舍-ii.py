#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
from typing import List
from functools import cache

# 注意len(nums) == 1 是的边界条件
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(start, end):
            if start < end:
                if start == end - 1:
                    return nums[start]
                ans1 = nums[start] + dp(start + 2, end)
                ans2 = dp(start + 1, end)
                return max(ans1, ans2)
            else:
                return 0
        if len(nums) == 1:
            return nums[0]   
        return max(dp(0, len(nums) - 1), dp(1, len(nums) ))

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(start, end):
            rob, not_rob = 0, 0
            for i in range(start, end):
                rob, not_rob = not_rob + nums[i], max(rob, not_rob)
            return max(rob, not_rob)
        if len(nums) == 1:
            return nums[0]
        return max( dp(0, len(nums) - 1), dp(1, len(nums)))
# @lc code=end

