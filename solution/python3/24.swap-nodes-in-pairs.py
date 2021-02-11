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

        count = 1
        prev = None
        current = dummy
        while head:
            if count % 2 == 0:
                current.next = ListNode(head.val)
                current.next.next = ListNode(prev.val)
                current = current.next.next
            prev = head
            print(head.val)
            head = head.next
            count += 1

        if count % 2 == 0:
            current.next = ListNode(prev.val)
        return dummy.next

# @lc code=end

