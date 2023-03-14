#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start

# maxBuy 从尾部开始记录当前出售最大值
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, maxSell = 0, prices[-1]
        for v in prices[::-1]:
            maxSell = max(maxSell, v)
            res = max(res, maxSell - v)
        return res

# minBuy 记录当前购入最小值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minBuy = 0, prices[0]
        for v in prices:
            minBuy = min(v, minBuy)
            res = max(res, v - minBuy)
        return res

# 运用labuladong分析的套路公式进行分析
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        
        for i in range(len(prices)):
            if not i:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1],  - prices[i])
            #print(dp[i])
        return dp[len(prices) - 1][0]

# 对上一个空间动态规划优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty, have = 0, -prices[0]
        for i in range(1, len(prices)):
            empty, have = max(empty, have + prices[i]), max(have, -prices[i])
        return empty
# @lc code=end
# obj = Solution()
# prices = [7,1,5,3,6,4]
# obj.maxProfit(prices)

