#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
# 法一：参考380.o-1-时间插入，删除和等概率获取随机元素，但是忽略了整数n的条件
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        if n < 1e9:
        
            self.l = list(range(n))
            self.d = {self.l[i]:i for i in range(n)}
            for v in blacklist:
                self.remove(v)
        else:
            
            self.s = set(blacklist)

    def remove(self, val):
        idx = self.d[val]
        lastVal = self.l[len(self.l) - 1]
        self.d[lastVal], self.l[idx] = idx, lastVal
        self.d.pop(val)
        self.l.pop()
    def pick(self) -> int:
        if self.n < 1e9:
            return choice(self.l)
        else:
            res = choice(range(self.n))
            while res  in self.s:
                res = choice(range(self.n))
            return res
            
#法二： 减小内存占用
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.sz = n - len(blacklist)
        self.d = {b:666 for b in blacklist}
        last = n - 1
        for v in blacklist:
            if v >= self.sz:
                continue
            while last in self.d:
                last -= 1
            self.d[v] = last
            last -= 1

    def pick(self) -> int:
        res = choice(range(self.sz))
        if res in self.d:
            return self.d[res]
        else:
            return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

