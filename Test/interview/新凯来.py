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