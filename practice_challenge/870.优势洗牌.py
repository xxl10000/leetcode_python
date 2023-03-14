#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
import bisect
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        visited = [False] * len(nums1)
        res = []

        for i,v in enumerate(nums2):
            idx = bisect.bisect(nums1, v)
            while idx < len(nums1) and visited[idx]:
                idx += 1
            
            if idx == len(nums1):
                idx = visited.index(False)
            
            visited[idx] = True
            res.append(nums1[idx])
        return res
# @lc code=end

