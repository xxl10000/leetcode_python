#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# @lc code=start
# 采用单调队列的方法，队列头为长度为k里面的最大值，同时用字典存储值及最近一次的下标，来判断单调队列中对应索引长度是否等于k
from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, deq = [],deque()
        d = {}
        for idx,v in enumerate(nums):
            if deq and d[deq[-1]] - d[deq[0]] >= k - 1:
                d.pop(deq[0])
                deq.popleft()
            while deq and deq[-1] <= v:
                d.pop(deq[-1])  
                deq.pop()              
            
            deq.append(v)
            d[v] = idx
            
            
            if idx >= k - 1:
                res.append(deq[0])
        return res

# 可以用nums[i - k + 1] 是否和单调队列头相等来判断是否长度超过k
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, q = [], deque()
        for i, v in enumerate(nums):
            
            while q and q[-1] < v:
                q.pop()
            q.append(v)
            if i >= k - 1:
                res.append(q[0])
                if nums[i - k + 1] == q[0]:
                    q.popleft()
        return res
            
            
         
# @lc code=end

