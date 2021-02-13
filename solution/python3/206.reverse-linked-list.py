#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        dummy = current = ListNode()
        while head:
            stack.append(head)
            head = head.next

        while stack:
            node = stack.pop()
            current.next = ListNode(node.val)
            current = current.next
        return dummy.next

# @lc code=end

