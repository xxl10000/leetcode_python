#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                pos = [(0,1), (0, -1), (1, 0), (-1, 0)]
                
                for p in pos:
                    next_i = i + p[0]
                    next_j = j + p[1]
                    dfs(next_i, next_j)
        
        for i in [0, m - 1]:
            for j in range(n):
                if not grid[i][j]:
                    dfs(i, j)
        
        for j in [0, n - 1]:
            for i in range(m):
                if not grid[i][j]:
                    dfs(i,j)
        
        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not grid[i][j]:
                    dfs(i, j)
                    res += 1
        return res
# @lc code=end

