#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start

from typing import List

# dp O(N)
# f(n) 记录截止下标为n的时候最大子数组和
# f(n) = max( f(n - 1) + nums[n], nums[n])
# 然后对 f(n) 遍历求最大值
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalMax = thisMax = float('-inf')
        for v in nums:
            thisMax = max(thisMax + v, v)
            totalMax = max(thisMax, totalMax)
        return totalMax

# 分治解法 O(NlogN) 超时 200/210
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def conMidMax(idx):
            leftSum = rightSum = 0
            leftAns = rightAns = -float('inf')
            for i in range(idx - 1, -1, -1):
                v = nums[i]
                leftSum += v
                leftAns = max(leftSum, leftAns)
            for v in nums[idx:]:
                rightSum += v
                rightAns = max(rightSum, rightAns)
            leftAns = max(leftAns, 0) # 注意分治解法的条件，可以
            
            return leftAns + rightAns
        
        def maxSub(start, end):
            if start == end:
                return -float('inf') #无实际意义的返回值，并不是0，为了不给求最大值造成干扰，取一个最小值
            
            mid = start + (end - start) // 2
            
            return max(maxSub(start, mid),  conMidMax(mid), maxSub(mid + 1, end) )
        mid = len(nums) // 2
        #print(conMidMax(mid))
        return max(  conMidMax(mid), maxSub(0, mid),maxSub(mid + 1, len(nums)) )

# 画图理解， minBuy 代表preSum[0...i]的最小值，要求最大和的连续子数组，即preSum[i + 1] - minBuy的最大值
# 这样能保证最值的对应顺序，而不是简简单单的preSum里面最大 - 最小
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        preSum = [0] * (len(nums) + 1)
        preSum[0] = 0
        for i in range(1,len(nums) + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        minBuy = float('inf')
        res = float('-inf')
        # 不好理解，这完全是面向测试用例编程
        # for v in preSum:
        #     res = max(res, v - minBuy)
        #     minBuy = min(minBuy, v)
        for i in range(len(nums)):
            minBuy = min(minBuy, preSum[i])
            res = max(res, preSum[i + 1] - minBuy)
            
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        left = right = 0
        res = float('-inf')
        thisSum = 0
        while right < len(nums):
            rNumber = nums[right]
            right += 1
            thisSum += rNumber
            res = max(res, thisSum)
            while thisSum < 0:
                lNumber = nums[left]
                left += 1
                thisSum -= lNumber
                # 加了这个 thisSum = 0 会有可能成为最值
                #res = max(res, thisSum)
            
        return res
            
# @lc code=end
obj = Solution()
print(obj.maxSubArray([-2,-1]))

