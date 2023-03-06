#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
# 回溯，处理枝条
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         res, onpath = [], []
        
#         def backtrack(start):
#             nonlocal res, onpath
            
#             if start == len(graph) - 1:
#                 res.append(onpath[:])
            
#             for neighbor in graph[start]:
#                 onpath.append(neighbor)
#                 backtrack(neighbor)
#                 onpath.pop()
            
#         onpath.append(0)
#         backtrack(0)
#         return res

# dfs, 处理结点 注意结束条件，如果直接return，还要前面加上pop()
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         res, onpath = [], []
        
#         def dfs(start):
#             nonlocal res, onpath
            
#             onpath.append(start)
            
#             if start == len(graph) - 1:
#                 res.append(onpath[:])
                
            
#             for neighbor in graph[start]:
#                 dfs(neighbor)
            
#             onpath.pop()
        
#         dfs(0) 
#         return res    

# bfs 主要怎么进队列和进队列的参数 
from collections import deque
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, onpath = [], []
        queue = deque()
        onpath.append(0)
        queue.append((0, onpath))
        
        while queue:
            sz = len(queue)
            for i in range(sz):
                node, path = queue.popleft()
                if node == len(graph) - 1:
                    res.append(path[:])
                for neighbor in graph[node]:
                    # 法1
                    #queue.append((neighbor, path + [neighbor]))
                    
                    # 法2， 传入参数为path[:]，不是path，原因同复制一个列表，不然会改变
                    path.append(neighbor)
                    queue.append((neighbor,path[:]))
                    path.pop()
        return res
        
# @lc code=end

a = [1]
print(id(a))
a.append(1)
print(id(a))
a.pop()
print(id(a))
print(id(a[:]))
b = a + []
print(id(b))
print(id(a + []))