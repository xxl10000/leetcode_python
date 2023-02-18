#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
# 该方法感觉技巧分析性太强了，尝试用labuladong的滑动窗口模板
# window 记录字符离right位置最近的下标
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right= 0, 0
        window = dict()
        res = 0
        while right < len(s):
            cR = s[right]
            if cR in window:
                left = max( window[cR] + 1, left)
            res = max(res, right - left + 1)
            window[cR] = right  #更新下标到最新，不论是否重复
            right += 1
        return res

#window 记录[left, right]的字符重复次数
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = Counter()
        res = 0
        while right < len(s):
            cRight = s[right]
            right += 1
            window[cRight] += 1
            while window[cRight] > 1:
                cLeft = s[left]
                left += 1
                window[cLeft] -= 1
            res = max(res, right - left)
        return res     
# @lc code=end

