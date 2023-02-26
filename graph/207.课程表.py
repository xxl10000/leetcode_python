#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for to, fro in prerequisites:
            graph[fro].append(to)
            inDegree[to] += 1
        
        d = deque([i for i in range(len(inDegree)) if inDegree[i] == 0])
        count = 0
        while d:
            sz = len(d)
            for i in range(sz):
                node = d.popleft()
                count += 1
                for neighbor in graph[node]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        d.append(neighbor)
        return count == numCourses     
# @lc code=end

