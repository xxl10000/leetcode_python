#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
from typing import List

# 法1：记 a = mx + n, 将 a^b -> n^b, 然后对b分奇偶数二分求余 效率：5.68%
# 可以用尾递归优化吗？

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        X = 1337
        n = a % X
        number = 0
        # for v in b:
        #     number = number * 10 + v
            
        def getNumber(a, b, res = 1):
            if b == 1:
                return (a * res) % X
            if b % 2:
                #return ((getNumber(a, b // 2))** 2 * a ) % X
                #return ((getNumber(a, b // 2) % X)** 2 * a ) % X
                return getNumber(a, b-1, res * a % X)
            else:
                #return ((getNumber(a, b // 2) % X) ** 2 ) % X
                return getNumber(a * a % X, b //2, res)
        
        #return getNumber(n, number)
        return pow(n, int(''.join(map(str,b))), X)


# 将b递归分解成两部分，分别求对X = 1337 的模，然后结果相乘再求模
# b 不一定要 b/2这样分解，可以按照对10求余和取模分成两部分
# (a^b) % X = (n^b)%X

# class Solution:
#     def superPow(self, a: int, b: List[int]) -> int:
#         X = 1337
#         a = a % X
#         def smallPow(a, k):
#             res = 1
#             for i in range(k):
#                 res = (res * a) % X
#             return res
#         def divideList(a, b):
#             if not b:
#                 return 1
#             last = b.pop()
#             part1 = smallPow(a, last)
#             #part2 = divideList(a, b) ** 10
#             part2 = smallPow(divideList(a, b), 10)
#             return (part1 * part2) % X
#         return divideList(a, b)

# class Solution:
#     def superPow(self, a: int, b: List[int]) -> int:
#         X = 1337
#         a = a % X
#         def smallPow(a, k):
#             res = 1
#             for i in range(k):
#                 res = (res * a) % X
#             return res
#         def divideList(a, b):
#             if not b:
#                 return 1
#             last = b.pop()
#             part1 = a ** last % X
#             #part2 = divideList(a, b) ** 10
#             part2 = (divideList(a, b) ** 10) % X
#             return (part1 * part2) % X
#         return divideList(a, b)   

# class Solution:
#     def superPow(self, a: int, b: List[int]) -> int:
#         return pow(a, int(''.join(map(str, b))), 1337)      
# @lc code=end
obj = Solution()
a = 2147483647
b = [2,0,0]

# a = 2
# b = [1, 0]
res = obj.superPow(a,b)
print(res)
