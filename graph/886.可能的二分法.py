#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
# 同785.判断二分图，只需要把dislikes转变成图用邻接表表示即可。注意图大小可以n+1，更加直观简单
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def dfs(i):
            for neighbor in graph[i]:
                if  visited[neighbor] == visited[i]:
                    return False
                elif not visited[neighbor]:
                    visited[neighbor] = 2 if visited[i] == 1 else 1
                    if not dfs(neighbor):
                        return False
            return True
        
        graph = [[ ] for _ in range(n)]
        for i, j in dislikes:
            graph[i - 1].append(j - 1)
            graph[j - 1].append(i - 1)
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
            if not dfs(i):
                return False
        return True
 
# 注意visited数组的判断，不用重复判断，更不要将上一次判断x后结果y继续当x处理 
from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(root):
            d = deque()
            if not visited[root]:
                visited[root] = 1
                d.append(root)
            while d:
                sz = len(d)
                for i in range(sz):
                    node = d.popleft()
                    #print(visited)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = 2 if visited[node] == 1 else 1
                            d.append(neighbor)
                        else:
                            if visited[neighbor] == visited[node]:
                                return False
            return True
        graph = [[ ] for _ in range(n + 1)]
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        visited = [0] * (n + 1)
        #print(graph)
        for i in range(n + 1):
            # if visited[i] == 0:
            #     visited[i] = 1
            if not bfs(i):
                return False
        return True
        
    
# @lc code=end

