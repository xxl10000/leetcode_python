#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
# 思路同567.字符串的排列，无非是不立刻返回布尔值，而是记录起始下标left
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter(p)
        left, right = 0, 0
        count = len(window)
        res = []
        while right < len(s):
            cRight = s[right]
            right += 1
            window[cRight] -= 1
            if window[cRight] == 0:
                count -= 1
            if right > len(p):
                cLeft = s[left]
                left += 1
                window[cLeft] += 1
                if window[cLeft] == 1:
                    count += 1
            if count == 0:
                res.append(left)
        return res
        
  
# @lc code=end

