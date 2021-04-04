/*
 * @lc app=leetcode id=141 lang=java
 *
 * [141] Linked List Cycle
 */

// @lc code=start
// Definition for singly-linked list.
// class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int x) {
//         val = x;
//         next = null;
//     }
// }
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode runner = head;
        ListNode walker = head;

        while (true) {
            if (walker.next != null) {
                walker = walker.next;
            } else {
                return false;
            }

            if (runner.next != null && runner.next.next != null) {
                runner = runner.next.next;
            } else {
                return false;
            }

            if (walker.equals(runner)) {
                return true;
            }
        }

    }
}
// @lc code=end

