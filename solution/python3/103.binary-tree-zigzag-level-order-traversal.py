#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = [root]
        level = 1
        while root and queue:
            tmp = queue[:]
            queue = []
            nodes = []
            for n in tmp:
                nodes.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            ans.append(nodes if level % 2 == 1 else list(reversed(nodes)))
            level += 1

        return ans


# @lc code=end

