from typing import List
from functools import cache
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        p1, p2, p = 0, 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][0] == nums2[p2][0]:
                res.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p , p1, p2 = p + 1, p1 + 1, p2 + 1
            elif  nums1[p1][0] < nums2[p2][0]:
                res.append([nums1[p1][0], nums1[p1][1] ])
                p , p1 = p + 1, p1 + 1    
            else:
                res.append([nums2[p2][0],  nums2[p2][1]])
                p , p2 = p + 1,  p2 + 1                        
        if p1 < len(nums1):
            res += nums1[p1:]
        if p2 < len(nums2):
            res += nums2[p2:]
        return res 
    
class Solution:
    def minOperations(self, n: int) -> int:
        s = set(2 **i for i in range(20))
        @cache
        def  dp(n):
            if n in s:
                return 1
            else:
                digit = len(bin(n)) - 2
                res1 = ( dp(2 ** digit - n))
                res2 =   dp(n - 2 **(digit - 1))      
                return 1 + min( dp(2 ** digit - n), dp(n - 2 **(digit - 1)))
                
        
        
        return dp(n)

class Solution1:
    
    def squareFreeSubsets(self, nums: List[int]) -> int:
        res = 0
        path = [0] * 30
        prime = set([2,3,5,7,11,13,17,19,23,29])
        
        @cache
        def put(x):
            
            if x == 1:
                return 
            if x in prime:
                path[x] += 1
            else:
                for elem in  prime:
                    if x // elem == 0:
                        path[elem] += 1
                        return put(x //elem)
        @cache
        def remove(x):
            if x == 1:
                return 
            if x in prime:
                path[x] -= 1
            else:
                for elem in  prime:
                    if x // elem == 0:
                        path[elem] -= 1
                        return put(x //elem)          
        
        def backtrack(n):
            res += 1
            for i in range(n, len(nums)):
                flag = True
                v = nums[i]
                path.put(v)
                for v in path:
                    if v >= 2:
                        flag = False
                if not flag:
                    path.remove(v)
                    continue
                backtrack(i + 1)
                path.remove(v)
        
        
        backtrack(0)
        return res
obj = Solution1()
print((obj.squareFreeSubsets([1,2,3,1])))