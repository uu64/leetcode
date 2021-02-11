#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(None)
        while True:
            if not l1 and not l2:
                break


            current.next = ListNode(None)
            current = current.next

            l1val = l1.val if l1 else 101
            l2val = l2.val if l2 else 101

            if l1val < l2val:
                current.val = l1val
                l1 = l1.next
            else:
                current.val = l2val
                l2 = l2.next

        return head.next

# @lc code=end

