#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start

# 没有思路的代码，思路不清晰的代码
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         numsSum = sum(nums)
#         if numsSum % k:
#             return False
#         avg = numsSum // k
#         nums.sort()
        
#         onpath, pathSum = [], 0
#         visited = [False] * len(nums)
        
#         res = []
#         def backtrack(start, count):
#             nonlocal pathSum, avg, onpath
#             if count == 0:
#                 return True
#             if pathSum == avg:
#                 pathSum = 0
                
#                 res.append(onpath[:])
                
#                 if backtrack(start, count - 1):
#                     return True
#                 #res.pop()
#             for i in range(start, len(nums)):
#                 if visited[i]:
#                     continue
#                 visited[i] = True
#                 onpath.append(nums[i])
#                 pathSum += nums[i]
#                 if (backtrack(i + 1, count)):
#                     return True
#                 pathSum -= nums[i]
#                 onpath.pop()
#                 visited[i] = False
#             return False
        
#         ans = backtrack(0, k)
#         print(res)
#         return ans

# 将n个球尝试放入值为avg的k个桶，一个一个球去遍历
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numsSum = sum(nums)
        if numsSum % k:
            return False
        avg = numsSum // k
        nums.sort(reverse=True)
        if nums[0] > avg:
            return False
        bucket = [0] * k
        
        def backtrack(start):
            nonlocal  avg
            if start == len(nums):
                return bucket.count(avg) == k
            
            for i in range(k):
                if nums[start] + bucket[i] > avg:
                    continue
                
                bucket[i] += nums[start]
                if (backtrack(start + 1)):
                    return True
                bucket[i] -= nums[start]
                if bucket[i] == 0:
                    break #并不用一个全局变量去退出所有递归，因为这只是局部的失败，可能bucket[0:i-1] 占用了太多较小量导致后面无法匹配
            return False
        
        ans = backtrack(0)
        #print(res)
        return ans

# 将值为avg的k个桶依次去放入n个球，一个一个桶去遍历      
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numsSum = sum(nums)
        if numsSum % k:
            return False
        avg = numsSum // k
        bucket = [0] * k
        visited = [False] * len(nums)
        nums.sort(reverse=True)
        def backtrack(idx, start):
            nonlocal avg
            if idx == k:
                return True
            if bucket[idx] == avg:
                return backtrack(idx + 1, 0)
            if bucket[idx] > avg:
                return False  
            for i in range(start, len(nums)):
                if visited[i]:
                    continue
                if bucket[idx] + nums[i] > avg:
                    continue
                visited[i] = True
                bucket[idx] += nums[i]
                
                if (backtrack(idx, i + 1)):
                    return True
                
                bucket[idx] -= nums[i]
                visited[i] = False
                if bucket[idx] == 0:   # 最重要的剪枝优化之一
                    break
            return False
        return backtrack(0, 0)
        
# @lc code=end

