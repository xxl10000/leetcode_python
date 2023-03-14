'''
给定一个字符串s，找到s中最长的回文子串的长度。
示例1：
输入：s = "babad"
输出：3
示例2：
输入：s = "cbbd"
输出：2
'''

class Solution:
    def Length(self, s):
        def getLength(pos1, pos2):
            while pos1 >= 0 and pos2 < len(s) and s[pos1] == s[pos2]:
                pos1 -= 1
                pos2 += 1
            return pos2 - pos1 - 1
            
        res = 1
        for i in range(len(s)):
            l1 = getLength(i,i)
            l2 = getLength(i, i + 1)
            res = max(res, l1, l2)
        return res
obj = Solution()
print(obj.Length('babad'))
print(obj.Length('cbbd'))