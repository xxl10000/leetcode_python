#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
# 本质上就是全排列46题用的回溯框架，可以把visited数组并入isPermit函数里面
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        graph = ['.'*n ] * n
        visited = [False] * n
        def isPermit(row, col):
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if graph[i][j] == 'Q':
                    return False
                i , j = i - 1, j - 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if graph[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1
            return True  
        def backtrack(idx):
            if idx == n :
                res.append(graph[:])
                return
            for i in range(n):
                if not visited[i] and isPermit(idx, i):
                    visited[i] = True
                    graph[idx] = graph[idx][:i] + 'Q' + graph[idx][i+1:]
                    backtrack(idx + 1)
                    visited[i] = False
                    graph[idx] = '.' * n
                    
                
        backtrack(0)
        return res
# @lc code=end

