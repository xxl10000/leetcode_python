#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start

# 法一：将原来全排列题46.结果去重，注意用生成式语法比较简单明了
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res, onpath = [], []
#         visited = [False] * len(nums)
#         def backtrack():
#             if len(onpath) == len(nums):
#                 res.append(onpath[:])
#                 return
#             for i in range(len(nums)):
#                 if visited[i]:
#                     continue
#                 visited[i] = True
#                 onpath.append(nums[i])
#                 backtrack()
#                 visited[i] = False
#                 onpath.pop()
#         backtrack()
#         s = set(tuple(v) for v in res)
#         res = list(list(t) for t in s)
#         return res

# if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1] 剪枝 确保 2->2'->2''这样的相对顺序
# 如果 not visited[i - 1] 变 visited[i - 1]，剪枝确保的顺序为 2''->2'->2，剪枝效率相对较低
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res, onpath = [], []
#         visited = [False] * len(nums)
#         nums.sort()
#         def backtrack():
#             if len(onpath) == len(nums):
#                 res.append(onpath[:])
#                 return
#             for i in range(len(nums)):
#                 if visited[i]:
#                     continue
#                 if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
#                     continue
#                 visited[i] = True
#                 onpath.append(nums[i])
#                 backtrack()
#                 visited[i] = False
#                 onpath.pop()
#         backtrack()
        
#         return res

# 用prevNum减去同一层次相等枝条。
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, onpath = [], []
        visited = [False] * len(nums)
        nums.sort()
        def backtrack():
            if len(onpath) == len(nums):
                res.append(onpath[:])
                return
            prevNum = 666
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if prevNum == nums[i]:
                    continue
                prevNum = nums[i]
                visited[i] = True
                onpath.append(nums[i])
                backtrack()
                visited[i] = False
                onpath.pop()
        backtrack()
        
        return res

# @lc code=end

