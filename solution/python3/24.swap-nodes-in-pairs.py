#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()

        current = dummy
        while head:
            if head.next:
                current.next = ListNode(head.next.val)
                current.next.next = ListNode(head.val)
                current = current.next.next
                head = head.next.next
            else:
                current.next = ListNode(head.val)
                break

        return dummy.next

# @lc code=end

