/*
 * @lc app=leetcode id=142 lang=java
 *
 * [142] Linked List Cycle II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode walker = head;
        ListNode runner = head;
        while (true) {
            if (walker.next != null) {
                walker = walker.next;
            } else {
                return null;
            }

            if (runner.next != null && runner.next.next != null) {
                runner = runner.next.next;
            } else {
                return null;
            }

            if (walker.equals(runner)) {
                break;
            }
        }

        while (true) {
            if (head.equals(walker)) {
                return head;
            }
            walker = walker.next;
            head = head.next;
        }
    }
}
// @lc code=end

