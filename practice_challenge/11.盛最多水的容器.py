#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start

# brute force, Time Limit Exceeded
# 50/61 cases passed (N/A)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, (j - i) * min(height[i], height[j]))
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            if height[right] > height[left]:
                res = max(res, (right - left) * height[left])
                left += 1
            else:
                res = max(res, (right - left) * height[right])
                right -= 1
        return res
# @lc code=end

