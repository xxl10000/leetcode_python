#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        dp = [[0] * (amount + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for j in range(1, n +  1):
            dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        
        return dp[m][n]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        # dp = [[0] * (amount + 1) for _ in range(m + 1)]
        # for i in range(m + 1):
        #     dp[i][0] = 1
        # for j in range(1, n +  1):
        #     dp[0][j] = 0
        dp = [1] + [0] * amount
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j < coins[i - 1]:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j] + dp[j - coins[i - 1]]
        
        return dp[n]
# @lc code=end

