#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
# 同52
class Solution:
    def totalNQueens(self, n: int) -> int:
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
            #global res
            #nonlocal res
            if idx == n :
                nonlocal res
                res += 1
                return
            for i in range(n):
                if not visited[i] and isPermit(idx, i):
                    visited[i] = True
                    graph[idx] = graph[idx][:i] + 'Q' + graph[idx][i+1:]
                    backtrack(idx + 1)
                    visited[i] = False
                    graph[idx] = '.' * n
                    #graph = []
                    
         
        #global res
        res = 0
        graph = ['.'*n ] * n
        visited = [False] * n
               
        backtrack(0)
        return res
obj = Solution()
print(obj.totalNQueens(5))
# @lc code=end

