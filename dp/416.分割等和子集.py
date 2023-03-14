#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        m, n= len(nums) , total // 2 
        dp = [[False] * (n + 1) for _ in range(m + 1) ]
        
        for i in range(m + 1):
            dp[i][0] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] | (dp[i - 1][j - nums[i - 1]])
        
        return dp[m ][n ]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        m, n= len(nums) , total // 2 
        # dp = [[False] * (n + 1) for _ in range(m + 1) ]
        
        # for i in range(m + 1):
        #     dp[i][0] = True
        dp = [True] + [False] * n

        for i in range(1, m + 1):
            # for j in range(1, n + 1):
            for j in range(n , -1, -1):
                # if j - nums[i - 1] < 0:
                #     dp[i][j] = dp[i - 1][j]
                # else:
                #     dp[i][j] = dp[i - 1][j] | (dp[i - 1][j - nums[i - 1]])
                if j - nums[i - 1] < 0:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j] | dp[j - nums[i - 1]]
        return dp[n]
# @lc code=end
