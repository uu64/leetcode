#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.getNumbers(l1)
        n2 = self.getNumbers(l2)
        s = str(n1 + n2)
        ans = None
        for c in s:
            ans = ListNode(int(c), ans)
        return ans


    def getNumbers(self, node):
        if node.next != None:
            return self.getNumbers(node.next)*10 + node.val
        else:
            return node.val

# @lc code=end

