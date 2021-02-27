#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = self.search(root)
        return result[0]

    def search(self, root):
        minVal = root.val
        maxVal = root.val
        isValid = True
        if root.left:
            l = self.search(root.left)
            isValid = isValid and l[0] and l[2] < root.val
            minVal = min(minVal, l[1])
            maxVal = max(maxVal, l[2])

        if root.right:
            r = self.search(root.right)
            isValid = isValid and r[0] and root.val < r[1]
            minVal = min(minVal, r[1])
            maxVal = max(maxVal, r[2])

        return (isValid, minVal, maxVal)
# @lc code=end

