#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start

# 字符串存入字典法，注意边界条件即可，right对应右开边界，取不到。
# from typing import List
# from collections import Counter
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         window = Counter()
#         res = []
#         left, right = 0, 10
#         while right <= len(s):
#             sub = s[left:right]
#             left += 1
#             right += 1
#             window[sub] += 1
#             if window[sub] == 2:
#                 res.append(sub)
#         return res

# 字符串哈希化存入字典, ? 效率低下， 运行时间战胜 5% ？
# from typing import List
# from collections import Counter
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         nums = [0] * len(s)
#         for i, v in enumerate(s):
#             if v == 'A':
#                 nums[i] = 0
#             elif v == 'G':
#                 nums[i] = 1
#             elif v == 'C':
#                 nums[i] = 2
#             elif v == 'T':
#                 nums[i] = 3
        
#         scale = 4
#         digit = 10
        
#         scaleDigit = scale **(digit - 1)
#         hashValue = 0
#         window = Counter()
#         left = right = 0
#         res = []
#         while right < len(s):
#             hashValue = hashValue * scale + nums[right]
            
#             right += 1
            
            
#             if right - left == digit:
#                 window[hashValue] += 1
#                 if window[hashValue] == 2:
#                     res.append(s[left:right]) 
#                 hashValue -= nums[left] * scaleDigit
#                 left += 1
                
                 
            
#         return res
        
# from typing import List
# from collections import Counter
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         nums = [0] * len(s)
#         for i, v in enumerate(s):
#             if v == 'A':
#                 nums[i] = 0
#             elif v == 'G':
#                 nums[i] = 1
#             elif v == 'C':
#                 nums[i] = 2
#             elif v == 'T':
#                 nums[i] = 3
        
#         scale = 4
#         digit = 10
        
#         scaleDigit = scale **(digit - 1)
#         hashValue = 0
#         window = set()
#         left = right = 0
#         res = set()
#         while right < len(s):
#             hashValue = hashValue * scale + nums[right]
            
#             right += 1
            
            
#             if right - left == digit: 
#                 if hashValue not in window:
#                     window.add(hashValue)
#                 else:
#                     res.add(s[left:right])       
#                 hashValue -= nums[left] * scaleDigit
#                 left += 1                         
#         return list(res)

# from collections import defaultdict
# class Solution:
#     # @param s, a string
#     # @return a list of strings
#     def findRepeatedDnaSequences(self, s):
#         sequences = defaultdict(int)
#         for i in range(len(s)):
#             sequences[s[i:i + 10]] += 1
            
#         return [key for key, value in sequences.items() if value > 1]
     
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1#add 1 to the count
        return [key for key, value in sequences.iteritems() if value > 1] #extract the relevant keys
   
# @lc code=end
# obj = Solution()
# print(obj.findRepeatedDnaSequences('AAAAAAAAAAAAA'))

