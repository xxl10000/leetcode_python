#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] *(amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for v in coins:
                if i >= v:
                    dp[i] = min(dp[i], dp[i - v] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(x):
            
            if x == 0:
                return 0
            res = float('inf')
            for v in coins:
                if x >= v:
                    res = min(res, dp(x - v) + 1)
            return res 
        ans = dp(amount)
        return ans if ans != float('inf') else -1
# @lc code=end

