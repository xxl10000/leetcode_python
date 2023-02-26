#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLength(pos1, pos2):
            while pos1 >= 0 and pos2 < len(s) and s[pos1] == s[pos2]:
                pos1 -= 1
                pos2 += 1
            return (pos1 + 1, pos2 - 1)
            
        res = (0,0)
        for i in range(len(s)):
            res1 = getLength(i,i)
            res2 = getLength(i, i + 1)
            l1, l2, l0 = res1[1] - res1[0], res2[1]-res2[0], res[1] - res[0]
            if l1 > l0 and l1 > l2:
                res = res1
            if l2 > l0 and l2 > l1:
                res = res2
        return s[res[0]: res[1] + 1]
# @lc code=end

