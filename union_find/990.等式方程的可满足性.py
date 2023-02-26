#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
from typing import List
class Solution:
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self.s[root_a] = root_b
    def find(self, a):
        #idx = ord(a) - ord('a')
        if self.s[a] == a:
            return a
        self.s[a] = self.find(self.s[a])
        return self.s[a]
    def equationsPossible(self, equations: List[str]) -> bool:
        self.s = [i for i in range(26)]
        for v in equations:
            if v[1] == '=':
                a, b = ord(v[0]) - ord('a'), ord(v[3]) - ord('a')
                self.union(a, b)
        
        for v in equations:
            if v[1] == '!':
                a, b = ord(v[0]) - ord('a'), ord(v[3]) - ord('a')
                if self.find(a) == self.find(b):
                    return False
        return True
#obj = Solution()
#print(obj.equationsPossible(["f==a","a==b","f!=e","a==c","b==e","c==f"]))
# @lc code=end

