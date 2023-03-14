#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List

# wrong: 145/322 -> add flag and v, 237/322 -> 分析代码怎么写，有思路就肯定可以写出来
# 无非是将思路变成代码，复杂度还是比较高O(N * N * max(List))。
# 思路：确定一个合理的起点（非0，比相邻的右边高），然后根据起点的高度先寻找不小于其高度的终点，如果找不到，逐渐向下兼容
# 然后根据起点和终点
# 计算对应面积
class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = 0
        res = 0
        
        while right < len(height) and left < len(height) - 1:
            if not height[left] or height[left + 1] > height[left]:
                left += 1
                continue
            flag = True
            v = height[left]
            while flag and v:
                
                for i in range(left + 2, len(height)):
                    if height[i] >= v:
                        right = i
                        res += (right - left - 1) * v
                        #print(res, v, height[right], left)
                        for k in range(left + 1, right):
                            res -= height[k] if height[k] < v else v
                        left = right - 1
                        flag = False
                        #print(res)
                        break
                v -= 1
            
            left += 1
        return res


# 注意分析对应max的范围
class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        for i in range(1, len(height) - 1):
            #res += v if (v :=min(max(height[0:i]), max(height[i + 1:])) - height[i]) > 0 else 0
            res += min(max(height[0:i + 1]), max(height[i :])) - height[i]
        return res

# 对上一个优化，空间换时间，先用计算出0-i, i-end的值用列表保存
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        headMax, tailMax = [0] * len(height), [0] * len(height)
        headMax[0] = height[0]
        for i in range(1, len(height)):
            headMax[i] = max(headMax[i - 1], height[i])
        tailMax[-1] = height[-1]
        for i in range(len(height) - 2, 0, -1):
            tailMax[i] = max(tailMax[i + 1], height[i])
            
        # print(headMax)
        # print(tailMax)
        for i in range(1, len(height) - 1):
            #res += v if (v :=min(max(height[0:i]), max(height[i + 1:])) - height[i]) > 0 else 0
            res += min(headMax[i], tailMax[i]) - height[i]
        return res

# 对上一个继续优化，双指针，短板效应
class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0, len(height) - 1
        leftMax = rightMax = 0
        res = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax > rightMax:
                res += rightMax - height[right]
                right -= 1
            else:
                res += leftMax - height[left]
                left += 1
        return res
# @lc code=end
# obj = Solution()
# print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

