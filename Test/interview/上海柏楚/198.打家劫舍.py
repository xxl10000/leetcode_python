#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List
from functools import cache

# 可以将ans2的值优化一下，直接等于 fun(start + 1), 这样减少边界条件的讨论，而且算法清晰
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def fun(start):
            if start < len(nums):
                # if start == len(nums) - 1:
                #     return nums[start]
                ans1 = nums[start] + fun(start + 2)
                ans2 = fun(start + 1)
                return max(ans1, ans2)
            else:
                return 0
        
        return fun(0)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) )
        dp[-1] = nums[-1]
        if len(nums) >= 2:
            dp[-2] = max(nums[-2], nums[-1] )
        for i in range(len(nums) -3, -1, -1):
            # 可以减少不必要的边界条件讨论
            # if i == len(nums) - 3:
            #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            # else:
            #     dp[i] = max(nums[i] + dp[i + 2], nums[i + 1] + dp[i + 3])
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]
    
# 增加虚拟头结点类似的方法减少对边界条件的讨论，对上一个的优化
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)  + 2)
        
        for i in range(len(nums) -1, -1, -1):
            # 可以减少不必要的边界条件讨论
            # if i == len(nums) - 3:
            #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            # else:
            #     dp[i] = max(nums[i] + dp[i + 2], nums[i + 1] + dp[i + 3])
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]

# 压缩变量
class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp = [0] * (len(nums)  + 2)
        x1, x2 = 0, 0
        for i in range(len(nums) -1, -1, -1):
            x1, x2 = max(nums[i] + x2, x1), x1
            #dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return x1
        
# @lc code=end

