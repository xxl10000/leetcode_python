#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nums = [(ord(v) - ord('a')) for v in haystack]
        
        needleHash = 0
        for v in needle:
            needleHash = needleHash * 26 + ord(v) - ord('a')
        
        pathHash = 0
        left = right = 0
        
        scale = 26
        digit = len(needle)
        scaleDigit = scale **(digit - 1)
        #window = dict()
        while right < len(nums):
            pathHash = pathHash * scale + nums[right]
            right += 1
            if right - left == len(needle):
                if pathHash == needleHash:
                    return left
                
                pathHash -= nums[left] * scaleDigit
                left += 1
        return -1
        
# @lc code=end

