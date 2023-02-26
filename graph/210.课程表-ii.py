#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[ ] for _ in range(numCourses)]
        inDegree = [0 ] * numCourses
        for ai, bi in prerequisites:
            graph[bi].append(ai)
            inDegree[ai] += 1
        d = deque([i for i in range(len(inDegree)) if not inDegree[i]])
        res = []
        while d:
            sz = len(d)
            for i in range(sz):
                node = d.popleft()
                res.append(nodes)
                for neighbor in graph[node]:
                    inDegree[neighbor] -= 1
                    if not inDegree[neighbor]:
                        d.append(neighbor)
        return res if len(res) == numCourses else []
        
        
# @lc code=end

