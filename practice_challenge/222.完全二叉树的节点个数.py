#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution:
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        def traverse(root):
            nonlocal count
            if not root:
                return
            traverse(root.left)
            count += 1
            traverse(root.right)
        traverse(root)
        return count

class Solution:
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        l, r = root, root
        hl = hr = 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hl == hr:
            return 2 ** hr  - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

