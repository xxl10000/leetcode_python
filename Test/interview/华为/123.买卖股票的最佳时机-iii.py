#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start

# 直接将两次分割成两个一次求解，
# Time Limit Exceeded
# 202/214 cases passed (N/A)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def maxP(start, end):
            ans, minBuy = 0, prices[start]
            
            for i in range(start, end):
                minBuy = min(minBuy, prices[i])
                ans = max(ans, prices[i] - minBuy)
            return ans
        
        res = maxP(0, len(prices))
        for i in range(1, len(prices) - 1):
            if prices[i - 1] < prices[i] < prices[i + 1]:
                continue
            if prices[i - 1] > prices[i] > prices[ i + 1]:
                continue
            res = max(res, maxP(0, i) + maxP(i, len(prices)))
        return res

# 可以忽略 k == 0 情况， 然后从1 开始遍历
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, K = len(prices), 2
        dp = [[ [0] * 2 for _ in range(K + 1)] for _ in range(n)]
        
        for i in range(n):
            # for k in range(0, K + 1):
            for k in range(1, K + 1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                # if k == 0:
                #     dp[i][k][0] = 0
                #     dp[i][k][1] = -float('inf')
                #     continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][K][0]

# 对上一个进行空间复杂度优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i10 = dp_i20 = 0
        dp_i11 = dp_i21 = -float('inf')
        for v in prices:
            # tmp = dp_i10
            # dp_i10 = max(dp_i10, dp_i11 + v)
            # dp_i11 = max(dp_i11, 0 - v)
            # dp_i20 = max(dp_i20, dp_i21 + v)
            # dp_i21 = max(dp_i21, tmp - v)
            
            # 注重代码顺序，可以省一个临时变量
            dp_i20 = max(dp_i20, dp_i21 + v)
            dp_i21 = max(dp_i21, dp_i10 - v)
            
            dp_i10 = max(dp_i10, dp_i11 + v)
            dp_i11 = max(dp_i11, 0 - v)
            
        return dp_i20
# 别人方法的原代码，双线并进，同121 前两个解法分别记录最小，最大结合
# def maxProfit(self, prices):
#     if not prices:
#         return 0
    
#     # forward traversal, profits record the max profit 
#     # by the ith day, this is the first transaction
#     profits = []
#     max_profit = 0
#     current_min = prices[0]
#     for price in prices:
#         current_min = min(current_min, price)
#         max_profit = max(max_profit, price - current_min)
#         profits.append(max_profit)
    
#     # backward traversal, max_profit records the max profit
#     # after the ith day, this is the second transaction 
#     total_max = 0    
#     max_profit = 0
#     current_max = prices[-1]
#     for i in range(len(prices) - 1, -1, -1):
#         current_max = max(current_max, prices[i])
#         max_profit = max(max_profit, current_max - prices[i])
#         total_max = max(total_max, max_profit + profits[i])
        
#     return total_max
# @lc code=end

