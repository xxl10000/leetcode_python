#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# 注意空的情况套用回溯模板即可
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict ={'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res, onpath = [], ''
        
        def backtrack(start):
            nonlocal onpath
            if start == len(digits):
                res.append(onpath)
                return
            
            for val in dict[digits[start]]:
                onpath += val
                backtrack(start + 1)
                onpath = onpath[:-1]
                
        backtrack(0)
        return res
# @lc code=end

