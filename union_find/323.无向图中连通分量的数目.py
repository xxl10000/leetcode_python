from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            nonlocal parent
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal parent
            root_x = find(x)
            root_y = find(y)
            parent[root_x] = root_y
        parent = [i for i in range(n)]
        for x, y in edges:
            union(x, y)
        #print(parent)
        return len(set(find(i) for i in range(n) ))

# dfs和bfs遍历邻接表就可以，没必要去遍历邻接矩阵。
# dfs


class SolutionDFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dp(i, j):
            nonlocal matrix
            if 0 <= i < n and 0 <= j < n and matrix[i][j]:
                matrix[i][j] = False
                dp(i + 1, j)
                dp(i - 1, j)
                dp(i, j + 1)
                dp(i, j - 1)
        matrix = [[False] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = True
        for i, j in edges:
            matrix[i][j] = True
            matrix[j][i] = True

        res = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j]:
                    dp(i, j)
                    res += 1
        return res

# bfs:

from collections import deque
class SolutionBFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        matrix = [[False] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = True
        for i, j in edges:
            matrix[i][j] = True
            matrix[j][i] = True

        res = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j]:
                    res += 1
                    print(matrix)
                    q = deque()
                    q.append([i, j])
                    #matrix[i][j] = False
                    
                    while q:
                        sz = len(q)
                        for i in range(sz):
                            row, col = q.popleft()
                            if row + 1 < n and matrix[row + 1][col]:
                                q.append([row + 1,col])
                                matrix[row + 1][col] = False
                            if row - 1 >= 0 and matrix[row - 1][col]:
                                q.append([row - 1,col])
                                matrix[row - 1][col] = False
                            if col + 1 < n and matrix[row][col + 1]:
                                q.append([row,col + 1])
                                matrix[row][col + 1] = False
                            if col - 1 >= 0 and matrix[row][col - 1]:
                                q.append([row,col - 1])
                                matrix[row][col - 1] = False
        return res
n = 5 
edges = [[0, 1], [1, 2], [3, 4]]
edges1 = [[0, 1], [1, 2], [2, 3], [3, 4]]
l = [Solution(), SolutionDFS(), SolutionBFS()]
for v in l:
    print(v.countComponents(n, edges1))