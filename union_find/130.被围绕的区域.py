#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start

# 表面上是并查集，实际上还是图的邻接矩阵遍历，类似岛屿问题
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
       
            
        m, n = len(board), len(board[0])
        parent = [i for i in range(m * n + 1)]
        dummy = m * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            # return parent[x] if parent[x] == x else (parent[x]:=find(parent[x]))
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    union(n * i + j, dummy)
        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == 'O':
                    union(n * i + j, dummy)
        d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    for k in range(len(d)):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            union(n * x + y, n * i + j)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    if find(n * i + j) != find(dummy):
                        board[i][j] = 'X'
        
# @lc code=end

