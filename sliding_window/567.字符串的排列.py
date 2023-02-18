#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
# 注意分析是right = right + 1 后的 right 去对应边界条件，分析清楚边界条件套用labudong模板即可
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter(s1)
        left, right = 0, 0
        count = len(window)
        while right < len(s2):
            cRight = s2[right]
            right += 1
            window[cRight] -= 1
            if window[cRight] == 0:
                count -= 1
            
            if right > len(s1):  # not right + 1
                cLeft = s2[left]
                left += 1
                window[cLeft] += 1
                if window[cLeft] == 1:
                    count += 1
            
            if count == 0:
                return True
        return False
# @lc code=end

