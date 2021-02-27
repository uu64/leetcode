#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        d = deque(preorder)
        return self.construct(d, inorder)

    def construct(self, d, inorder):
        if not inorder:
            return None
        else:
            root = d.popleft()
            rootIdx = inorder.index(root)
            l = self.construct(d, inorder[:rootIdx])
            r = self.construct(d, inorder[rootIdx+1:])
            return TreeNode(root, l, r)


# @lc code=end

