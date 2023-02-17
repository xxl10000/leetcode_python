#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m , n = len(dungeon), len(dungeon[0])
        dp = [[[0, 1]for _ in range(n)]  for _ in range(m )]
        dp[0][0][0] = dungeon[0][0]
        dp[0][0][1] = dungeon[0][0]
        for i in range(1, m):
            dp[i][0][0] = dp[i - 1][0][0] + dungeon[i][0]
            dp[i][0][1] = min(dp[i][0][0], dp[i - 1][0][1])
        for j in range(1, n):
            dp[0][j][0] = dp[0][j - 1][0] + dungeon[0][j]
            dp[0][j][1] = min(dp[0][j][0], dp[0][j - 1][1])
        for i in range(1, m):
            for j in range(1, n):
                x1 = dp[i][j - 1][0] + dungeon[i][j]
                x2 = dp[i - 1][j][0] + dungeon[i][j]
                y1 = min(dp[i][j - 1][1], x1)
                y2 = min(dp[i - 1][j][1], x2)
                if y1 > y2:
                    dp[i][j][1] = y1
                    dp[i][j][0] = x1
                elif y2 > y1:
                    dp[i][j][1] = y2
                    dp[i][j][0] = x2
                else:
                    if x1 > x2:
                        dp[i][j][1] = y1
                        dp[i][j][0] = x1 
                    else:
                        dp[i][j][1] = y2
                        dp[i][j][0] = x2  
        print(dp)                     
        return max(1 - dp[m - 1][n - 1][1],1)
                
        
   
        
obj = Solution()
print(obj.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))

# @lc code=end

