#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
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
            if current.val < head.val:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return dummy.next




# @lc code=end

