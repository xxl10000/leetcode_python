#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start

#1. 起始位置都为0开始，找第一个两个字符串字符处不同的位置记为i
#2. 判断有无字符串从i开始为空集，如有，返回另外一个字符串从i开始后的长度
# （这个不能直接从word1[0]判断，有结果多加1的风险，比如word1 = 't',word2 = 't',就算比较后为空集，insert,delete,replace空集后最终结果也是1）
#  这样避免两相同字符串比较后从i开始为空集却返回1的情形
#3. 插入为word2[i], 那么比较word1[i:], word2[i + 1:]的最小数量即可，删除和替换同理，最后求三者最小值即可
from functools import cache
class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int: 
        i = 0
        while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
            i += 1
        if not word2[i:]:
            return len(word1[i:])
        if not word1[i:]:
            return len(word2[i:])
        insert = 1 + self.minDistance( word1[i:], word2[i + 1:])
        delete = 1 + self.minDistance(word1[i + 1:], word2[i:])
        replace = 1 + self.minDistance(word1[i + 1:], word2[i + 1:])
        return min(insert, delete, replace)
    
#优化方案：函数形式参数不用word[i:], 而是i，即 f(word[i]) -> f(i)，将word内置为一个常量
#dp(i, j) 函数定义为word1[i:] 到word2[j:]最小编辑距离，以终点，也就是word的末尾为base case,参考系
class Solution:  
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @cache
        def dp(i, j):
            nonlocal m, n
            while i < m and j < n and word1[i] == word2[j]:
                i ,j = i + 1, j + 1
            if not word1[i:]:
                return len(word2[j:])
            if not word2[j:]:
                return len(word1[i:])
            return 1 + min(dp(i + 1, j), dp(i + 1, j + 1), dp(i, j + 1)) # delete, replace, insert
        return dp(0, 0)

#同理，也可以通过自底而上的方法计算，之前由于传入是word[i]不好用嵌套列表分析，但是传入i就好用了，确定base case， 代码略
# @lc code=end

