#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
# 搜索区间为[left, right], 双闭区间， while 是 <=，可以从while 条件是
# 保证搜索区间非空，如[right + 1, right]是，才能保证该区间为空
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1

# 搜索区间为[left, right) 左闭右开区间， while 是 <
class Solution:
    def search(self, nums: List[int], target:int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1
# @lc code=end
