#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        runner = head
        walker = head
        while True:
            if runner is None or runner.next is None or runner.next.next is None:
                return False

            walker = walker.next
            runner = runner.next.next

            if walker == runner:
                return True


# @lc code=end

