# from typing import List
# from collections import deque
# from functools import cache
#都是以终点，也就是矩阵的第 n - 1列为终点，判断矩阵中每个元素到终点的下降路径最小和

#自底而上解法
class Solution:
    def minFallingPathSum(self, matrix) :
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        if n == 1:
            return matrix[0][0]
        for j in range(n):
            dp[n - 1][j] = matrix[n - 1][j]
        for i in range(n - 2, - 1, -1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j], dp[i + 1][j - 1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1], dp[i + 1][j - 1])
        return min(dp[0])

# # 自顶而下解法
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         @cache
#         def dp(i, j):
#             nonlocal n
#             if i < 0 or i >= n or j < 0 or j >= n:
#                 return 1e5
#             if i == n - 1:
#                 return matrix[i][j]
#             else:
#                 return matrix[i][j] + min(dp(i + 1, j), dp(i + 1, j +  1), dp(i + 1, j - 1))
        
#         res = 1e5
#         for j in range(n):
#             res = min(res, dp(0, j))
            
#         return res
    
# obj = Solution()
# x = obj.coinChange([1,2,5], 11)
# print(x)
