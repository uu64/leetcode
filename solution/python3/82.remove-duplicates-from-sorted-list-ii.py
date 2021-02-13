#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-101)
        current = dummy
        while True:
            if not head:
                break

            if head.val > current.val:
                count = 0
                while head.next and head.val == head.next.val:
                    count += 1
                    head = head.next
                if count == 0:
                    current.next = ListNode(head.val)
                    current = current.next

            head = head.next

        return dummy.next

# @lc code=end

