/*
 * @lc app=leetcode id=83 lang=java
 *
 * [83] Remove Duplicates from Sorted List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode dummy = new ListNode(-101);
        ListNode current = dummy;
        while (true) {
            System.out.println(head.val);
            if (head.next == null) {
                break;
            }
            if (head.val != current.val) {
                current.next = new ListNode(head.val);
                current = current.next;
            }
            head = head.next;
        }
        if (head.val != current.val) {
            current.next = new ListNode(head.val);
            current = current.next;
        }

        return dummy.next;

    }
}
// @lc code=end

