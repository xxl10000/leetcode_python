#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
# 时间复杂度不允许，8/15 通过 
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res, onpath = 0, []
        pathSum = 0
        nums.sort()
        
        ans = []
        def backtrack():
            nonlocal pathSum, res
            if pathSum == target:
                res += 1
                ans.append(onpath[:])
                return
            if pathSum > target:
                return
            
            for i in range(len(nums)):
                if pathSum + nums[i] > target:
                    break
                onpath.append(nums[i])
                pathSum += nums[i]
                backtrack()
                pathSum -= nums[i]
                onpath.pop()
                
        
        backtrack()
        for v in ans:
            print(v)
        return res
# @lc code=end
obj = Solution()
obj.combinationSum4([1,2,4], 8)
