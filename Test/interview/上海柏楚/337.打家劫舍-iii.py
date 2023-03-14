#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans1 = root.val
        ans2 = self.rob(root.left) + self.rob(root.right)
        if root.left:
            ans1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            ans1 += self.rob(root.right.left) + self.rob(root.right.right)
        return max(ans1, ans2)
# @lc code=end

