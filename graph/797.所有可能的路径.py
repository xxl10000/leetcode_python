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
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, onpath = [], []
        
        def dfs(start):
            nonlocal res, onpath
            
            onpath.append(start)
            
            if start == len(graph) - 1:
                res.append(onpath[:])
                
            
            for neighbor in graph[start]:
                dfs(neighbor)
            
            onpath.pop()
        
        dfs(0) 
        return res     
        
# @lc code=end

