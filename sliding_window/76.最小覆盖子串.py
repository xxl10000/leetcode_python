#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
# window表示s和t之间字符差异的具体数目，记t为正，s为负数。
# count 表示s和t字符差异的种类数
# 根据labudong 滑动窗口模板套用即可
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right , res= 0, 0, ''
        window = Counter(t)
        count = len(window)
        while right < len(s):
            cRight = s[right]
            right += 1
            window[cRight] -= 1
            if window[cRight] == 0:
                count -= 1
            while count == 0:
                cLeft = s[left]
                left += 1
                window[cLeft] += 1
                if window[cLeft] == 1:
                    count += 1
                    if not res:
                        res = s[left - 1: right]
                    if right - left + 1 < len(res): 
                        res = s[left - 1: right]
        return res   
# 小小的对上面优化，将复制字符串变成传递字符串的首尾，用start, end 和 s共同表示返回值
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right , start, end= 0, 0, 0, 0
        window = Counter(t)
        count = len(window)
        while right < len(s):
            cRight = s[right]
            right += 1
            window[cRight] -= 1
            if window[cRight] == 0:
                count -= 1
            while count == 0:
                cLeft = s[left]
                left += 1
                window[cLeft] += 1
                if window[cLeft] == 1:
                    count += 1
                    if start == 0 and end == 0:
                        start, end= left - 1, right
                    if right - left + 1 < end - start + 1: 
                        start, end= left - 1, right
        return s[start:end]              
# @lc code=end

