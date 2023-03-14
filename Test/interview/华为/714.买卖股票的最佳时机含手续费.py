#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        empty, have = 0, -float('inf')
        for v in prices:
            empty, have = max(empty, have + v ), max(have, empty - v - fee )
        return empty
# @lc code=end

