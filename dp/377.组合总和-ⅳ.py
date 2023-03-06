#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
# 时间复杂度不允许，8/15 通过 
from typing import List
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         res, onpath = 0, []
#         pathSum = 0
#         nums.sort()
        
#         ans = []
#         def backtrack():
#             nonlocal pathSum, res
#             if pathSum == target:
#                 res += 1
#                 ans.append(onpath[:])
#                 return
#             if pathSum > target:
#                 return
            
#             for i in range(len(nums)):
#                 if pathSum + nums[i] > target:
#                     break
#                 onpath.append(nums[i])
#                 pathSum += nums[i]
#                 backtrack()
#                 pathSum -= nums[i]
#                 onpath.pop()
                
        
#         backtrack()
#         for v in ans:
#             print(v)
#         return res

# 求最值问题联想到动态规划，建立状态转移方程 dp[n] = sum(dp[n - v] for v in nums if n >= v) 
# 因此会定义 dp[0] = 1 dp[n] 表示target 为n时候方案数
# 假定nums[i]为排列头或者尾或者固定一个位置，因此对nums 遍历求dp[n - nums[i]]的有效和即可
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        #nums.sort()
        dp[0] = 1
        for i in range(1, target + 1):
            dp[i] = sum(dp[i - v]  for v in nums if i >= v)
        #print(dp)
        return dp[target]
            
# @lc code=end
# obj = Solution()
# print(obj.combinationSum4([1,2,3], 5))
