#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
from typing import List

#以为k是站点名称，但是并不是，k表示数目
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if k == src:
            for fro, to, price in flights:
                if fro == src and to == dst:
                    return price
            return -1
        else:
            res = 0
            direct = -1
            for fro, to, price in flights:
                if fro == src and to == k:
                    res += price
                if fro == k and to == dst:
                    res += price
                if fro == src and to == dst:
                    direct = price
            if res == 0 and direct == -1:
                return -1
            else:
                return min(res, direct) if direct != -1 else res

# 回溯通过28/52 测试用例，超时
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[-1] * n for _ in range(n)]
        for fro, to , price in flights:
            graph[fro][to] = price
        #print(graph)
        res, onpath = -1, 0
        pathSum = 0
        def backtrack(start):
            nonlocal pathSum, res, onpath
            if start == dst and onpath <= k + 1:
                res = min(res, pathSum) if res != -1 else pathSum
                return
            if onpath > k:
                return
            for idx, price in enumerate(graph[start]):
                if price == -1:
                    continue
                
                onpath += 1
                pathSum += price
                backtrack(idx)
                pathSum -= price
                onpath -= 1
        
        backtrack(src)
        return res
    
# 未完成，尝试用动态规划,dp[i] 表示用且只用k个中转到达的最低价格，自己推不出状态转移方程
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for fro, to, price in flights:
            graph[fro].append((to, price))
        res = -1
        dp = [-1] * len(k + 1)
        
        return min([v for v in dp if v != -1])   

# 用出度表示，参考别人思路的递归解法
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for fro, to, price in flights:
            graph[fro].append((to, price))
        
        @functools.cache
        def dp(start, k):
            if start == dst:
                return 0
            if k < 0:
                return -1
            
            res = float('inf')
            for to, price in graph[start]:
                ans = dp(to, k - 1)
                if ans != -1:
                    res = min(res, ans + price)
            return res if res != float('inf') else -1
        
        return dp(src, k)  

#用入度表示，以终点为参考系，类似魔塔和子序列和问题，然后推导状态转移方程即可
import functools
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inDegree = [[] for _ in range(n)]
        for fro, to, price in flights:
            inDegree[to].append((fro, price))
        
        K = k + 1 # the number of edge of src to dst   
        
        @functools.cache
        def dp(end, edge):
            if end == src:
                return 0
            if edge == 1:
                for start, price in inDegree[end]:
                    if start == src:
                        return price
                return -1
            res = -1
            for newEnd, price in inDegree[end]:
                ans = dp(newEnd, edge - 1)
                if ans != -1:
                    res = min(res, ans + price) if res != -1 else ans + price
            return res
        
        return dp(dst, K)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k + 2 表示边数目为0,...,k + 1 时候对应最低价格
        dp = [ [float('inf')] * (k + 2) for _ in range(n)]
        dp[src][0] = 0
        
        for i in range(1, k + 2):
            for fro, to, price in flights:
                dp[to][i] = min(dp[to][i], dp[fro][i - 1] + price)
        res = min(dp[dst])
        return res if res != float('inf') else -1
# @lc code=end
obj = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src, dst, k = 0, 3, 1
print(obj.findCheapestPrice(n, flights, src, dst, k))
