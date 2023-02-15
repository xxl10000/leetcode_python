#
# @lc app=leetcode.cn id=1930 lang=python3
#
# [1930] 长度为 3 的不同回文子序列

#遍历字符串用字典存储不同字符第一次和最后一次出现位置，记为i, j，然后用集合判断s(i, j)不同字符数目
# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i, 0 ]
            else:
                d[s[i]][1] = i
        res = 0
        for values in d.values():
            start, end = values
            res += len(set(s[start + 1:end]))
        return res 
# @lc code=end

