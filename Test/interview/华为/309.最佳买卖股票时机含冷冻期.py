#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start

# 分析清楚关系， dp[i][flag]
# flag 1 -> flag 0 表示 从have -> empty, 也就是出售， 1 表示持有，0 表示不持有
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[ 0] * 2 for _ in range(len(prices))]
        
        for i in range(len(prices)):
            if i == 0:
                dp[0][0], dp[0][1] = 0, -prices[0]
                continue
            if i == 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[0][1], -prices[1])
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[len(prices) - 1][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty, having, preEmpty = 0, -float('inf'), 0
        for v in prices:
            empty, having, preEmpty = max(empty, having + v), max(having, preEmpty - v),empty
        return empty
# @lc code=end

