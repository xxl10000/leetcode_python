#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

# @lc code=start
from functools import cache
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #res = 0
        visited = [False] * len(points)
        
        #@cache
        def dfs(point, count, v):
            if count == len(points):
                return 0
            res = 0
            visited = list(v)
            for i, p in enumerate(points):
                if visited[i]:
                    continue
                visited[i] = True
                if res != 0:
                    res = min(res, 
                              dfs(p, count + 1, tuple(visited)) + abs(p[0] - point[0] ) + abs(p[1] - point[1]),
                              dfs(point, count + 1, tuple(visited))+ abs(p[0] - point[0] ) + abs(p[1] - point[1]))
                    
                else:           
                    res = min(dfs(p, count + 1,tuple(visited)) + abs(p[0] - point[0] ) + abs(p[1] - point[1]),
                              dfs(point, count + 1, tuple(visited))+ abs(p[0] - point[0] ) + abs(p[1] - point[1]))
                              
                
                visited[i] = False
            return res
        
        visited[0] = True
        v   = tuple(visited)
        ans =  dfs(points[0], 0, v)
        return ans
        
# @lc code=end
# obj = Solution()
# print( obj.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
