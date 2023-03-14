#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start

# 累加每一个可以赚钱的prices[i + 1] - prices[i] > 0, 则更新 minBuy = prices[i + 1]
# 可以画曲线图来理解， prices[i + 1] - prices[i] > 0 表示 一个相邻的增长段
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minBuy = 0, prices[0]
        for v in prices:
            if v > minBuy:
                res += v - minBuy
            minBuy = v
        return res

# 对上一个minBuy的优化，写成 prices[i + 1] - prices[i] 更容易直观理解
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(0, len(prices) - 1):
            res += max(prices[i + 1] - prices[i], 0)  
        return res

# 简简单单的列表生成式写法求和,亦可以额外加括号写成生成器
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum((max(prices[i + 1] - prices[i], 0) for i in range(0, len(prices) - 1)))
    

# labuladong 套路公式, 时间复杂度 O(N^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = K = len(prices)
        dp = [[[0] * 2 for _ in range(K + 1) ] for _ in range(n)]
        
        for i in range(n):
            for k in range(K + 1):
                if i == 0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        
        return dp[n - 1][K][0]

#  如何对上一个进行K 的空间优化，分析清楚各个变量即可
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = K = len(prices)
        dp = [[[0] * 2 for _ in range(2)]for _ in range(n)]
        
        for i in range(n):
            if i == 0:
                dp[0][0][0] = 0
                dp[0][0][1] = -prices[0]
                dp[i][1] = dp[i][0]
                continue
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
            
            dp[i][0] = dp[i][1]
        return dp[n - 1][0][0]

# k 趋于无穷大，假定k为 k - 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = K = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            
            
        return dp[n - 1][0]

# 对上一个进行动态规划空间复杂度优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty, have = 0, -float('inf')
        for v in prices:
            empty, have = max(empty, have + v), max(have, empty - v)
        return empty
# @lc code=end

