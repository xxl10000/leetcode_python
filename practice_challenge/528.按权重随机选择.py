#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
from typing import List

import bisect
import random

# 求对列表求前缀和，然后在前缀和里面取随机数，在二分搜索随机数所在范围
class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0] * (len(w) + 1)
        for i, v in enumerate(w):
            self.preSum[i + 1] = self.preSum[i] + w[i]
    def pickIndex(self) -> int:
        target = random.randint(1, self.preSum[-1])
        return bisect.bisect_left(self.preSum, target) - 1
       
# 将离散数据转变连续，可以忽略边界条件的细节
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        w = [ v/ total for v in w]
        self.preSum = [0] * len(w)
        start = 0
        for i,v in enumerate(w):
            start += v
            self.preSum[i] = start

    def pickIndex(self) -> int:
        target = random.random()
        return bisect.bisect(self.preSum, target)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
obj = Solution([1])
print(obj.pickIndex())
