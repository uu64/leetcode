#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = head
        runner = head
        while True:
            if not runner or not runner.next or not runner.next.next:
                return None

            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                break

        while True:
            if walker == head:
                return head
            walker = walker.next
            head = head.next

# @lc code=end

