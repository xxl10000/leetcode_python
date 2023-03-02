from typing import List
class Solution:
    def minMaxDifference(self, num: int) -> int:
        l = list(map(int, list(str(num))))
        max = l
        for i in range(len(max)):
            if max[i] != 9:
                tmp = max[i]
                for j in range(i, len(max)):
                    if max[j] == tmp:
                        max[j] = 9
                break
        maximum = int( ''.join(map(str, max)))
        min = l
        tmp = min[0]
        for i in range(len(max)):
            if min[i] == tmp:
                min[i] = 0 
        
        
        minimum = int( ''.join(map(str, min)))
        print(maximum, minimum)
        return maximum - minimum
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
        
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        a

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum1, sum2 = sum(nums1), sum(nums2)
        for idx, left, right in queries:
            if idx == 1:
                tmp = 0
                for i in range(left, right + 1):
                    nums1[i] = 0 if nums1[i] == 1 else 0
                    tmp += nums1[i]
                sum1 += (right + 1 - left) - 2 * tmp
            elif idx == 2:
                sum2 += left * sum1
            else:
                res.append(sum2)
        return res
from functools import cache          
class Solution1:
    
    def squareFreeSubsets(self, nums: List[int]) -> int:
        res = 0
        path = [0] * 30
        prime = set([2,3,5,7,11,13,17,19,23,29])
        
        @cache
        def put(x):
            nonlocal path, prime
            if x == 1:
                return 
            if x in prime:
                path[x] += 1
            else:
                for elem in  prime:
                    if x % elem == 0:
                        path[elem] += 1
                        put(x //elem)
                        break
        @cache
        def remove(x):
            nonlocal path, prime
            if x == 1:
                return 
            if x in prime:
                path[x] -= 1
            else:
                for elem in  prime:
                    if x % elem == 0:
                        path[elem] -= 1
                        put(x //elem)
                        break
        
        def backtrack(n):
            nonlocal res, path
            if n != 0:
                res += 1
            for i in range(n, len(nums)):
                flag = True
                v = nums[i]
                put(v)
                for s in path:
                    if s >= 2:
                        flag = False
                if not flag:
                    remove(v)
                    continue
                backtrack(i + 1)
                remove(v)
        
        
        backtrack(0)
        return res

obj = Solution1()
print(obj.squareFreeSubsets([3,4,4,5]))