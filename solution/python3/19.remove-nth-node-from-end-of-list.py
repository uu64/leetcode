#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        nodes = []

        if head.next == None:
            return None

        while True:
            nodes.append(node)
            if node.next == None:
                break
            node = node.next

        target = len(nodes) - n
        if target == len(nodes) - 1:
            nodes[-2].next = None
        elif target == 0:
            head = nodes[1]
        else:
            nodes[target - 1].next = nodes[target + 1]

        return head

# @lc code=end

