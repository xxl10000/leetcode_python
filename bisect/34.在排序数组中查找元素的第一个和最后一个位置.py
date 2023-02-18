#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
import bisect
class Solution:
    # 搜索左边界 [left, right)
    def searchLeftRange(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                right = mid
        #false: 没有判断nums[left] 不等于 target的情况，left越界和nums[left] == target都要考虑
        # return left  if left != len(nums) else -1   
        
        #因为left没有取到-1的可能，但是有可能取到len(nums)
        #即left取值范围为 [0, len(nums)]
        if left == len(nums):
            return -1
        return left if nums[left] == target else -1

    # # 搜索左边界 [left, right]
    # def searchLeftRange(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2
    #         if nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         elif nums[mid] == target:
    #             right = mid - 1
    #     if left == len(nums):
    #         return -1
    #     return left if nums[left] == target else - 1

    # 搜索右边界 [left, right)
    def searchRightRange(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                left = mid + 1
        #终止条件： 根据 left = mid + 1 推出 mid = left - 1 = right - 1
        if right - 1 < 0:
            return - 1
        return right - 1 if nums[right - 1] == target else -1 
    
    #调用bisect库，注意left, right的对应取值    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left ==len(nums):
            left = -1
        if nums[left] != target:
            left = -1
        right -= 1
        if right < 0:
            right = -1
        if nums[right] != target:
            right = -1
        return [left, right ]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeftRange(nums, target), self.searchRightRange(nums, target)] 

# @lc code=end

