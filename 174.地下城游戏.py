#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
from typing import List
# class Solution:
#     # 40/45 passed, can't pass [[1,-3,3],[0,-2,0],[-3,-3,-3]], answer 5, expected answer 3
#     # dp[i][j][1]:英雄血量从0开始后，从（0,0）到（i,j)的路线最低血量
#     # dp[i][j][0]:英雄血量从0开始后，从（0,0）到（i,j)根据最低血量路线计算的实时血量
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m , n = len(dungeon), len(dungeon[0])
#         dp = [[[0, 1]for _ in range(n)]  for _ in range(m )]
#         dp[0][0][0] = dungeon[0][0]
#         dp[0][0][1] = dungeon[0][0]
#         for i in range(1, m):
#             dp[i][0][0] = dp[i - 1][0][0] + dungeon[i][0]
#             dp[i][0][1] = min(dp[i][0][0], dp[i - 1][0][1])
#         for j in range(1, n):
#             dp[0][j][0] = dp[0][j - 1][0] + dungeon[0][j]
#             dp[0][j][1] = min(dp[0][j][0], dp[0][j - 1][1])
#         for i in range(1, m):
#             for j in range(1, n):
#                 x1 = dp[i][j - 1][0] + dungeon[i][j]
#                 x2 = dp[i - 1][j][0] + dungeon[i][j]
#                 y1 = min(dp[i][j - 1][1], x1)
#                 y2 = min(dp[i - 1][j][1], x2)
#                 if y1 > y2:
#                     dp[i][j][1] = y1
#                     dp[i][j][0] = x1
#                 elif y2 > y1:
#                     dp[i][j][1] = y2
#                     dp[i][j][0] = x2
#                 else:
#                     if x1 > x2:
#                         dp[i][j][1] = y1
#                         dp[i][j][0] = x1 
#                     else:
#                         dp[i][j][1] = y2
#                         dp[i][j][0] = x2  
#         print(dp)                     
#         return max(1 - dp[m - 1][n - 1][1],1)

#低 -> 上 ， dp[i][j]: (i,j)到（m-1,n-1)对应最低血量。类似迷宫从出口开始反推          
class Solution:  
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1 -(dungeon[m - 1][n - 1]) if (dungeon[m - 1][n - 1]) < 0 else 1
        
        #可以使用虚拟头结点，虚拟边界类似方法统一，外边界填充题目不可取得的大值。
        #dp = [[1e5] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = dp[i + 1][n - 1] - dungeon[i][n - 1]
            if dp[i][n - 1] <= 0:
                dp[i][n - 1] = 1
            
        for j in range(n - 2, -1 , -1):
            dp[m - 1][j] = dp[m - 1][j + 1] - dungeon[m - 1][j]
            if dp[m - 1][j] <= 0:
                dp[m - 1][j] = 1
        for i in range(m - 2, - 1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                if dp[i][j ] <= 0:
                    dp[i][j] = 1
        #print(dp)
        return dp[0][0]

# 顶 -> 下, dp(i, j): (i,j)到（m-1,n-1)对应最低血量。 
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                return 1 - dungeon[i][j] if dungeon[i][j] < 0 else 1
            
            if i == len(dungeon) or j == len(dungeon[0]):
                return 1e9
            
            res = min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j]
            if res <= 0:
                res = 1
            return res
        
        return dp(0, 0)  
             
#Debug       
# obj = Solution()
# print(obj.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))

# @lc code=end

