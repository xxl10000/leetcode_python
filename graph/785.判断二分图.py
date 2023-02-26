#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
# 二分图，用root 和neighbor 对应1或者2不同值去遍历图即可
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        def dfs(root):
            nonlocal visited
            # if visited[root] == 0:
            #     visited[root] = 1
            for neighbor in graph[root]:
                if visited[neighbor] != 0 and visited[neighbor] == visited[root]:
                    return False
                if visited[neighbor] == 0:
                    if visited[root] == 1:
                        visited[neighbor] = 2
                    else:
                        visited[neighbor] = 1
                    if not dfs(neighbor):
                        return False
            return True
        for i in range(len(graph)):
            if visited[i] == 0:
                visited[i] = 1
            if not dfs(i):
                return False
        return True
# @lc code=end

