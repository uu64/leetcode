/*
 * @lc app=leetcode id=703 lang=java
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
import java.util.*;

class KthLargest {
    private Queue<Integer> queue;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.queue = new PriorityQueue<Integer>();
        for (int i: nums) {
            this.add(i);
        }
    }

    public int add(int val) {
        this.queue.add(new Integer(val));
        if (this.queue.size() > this.k) {
            this.queue.poll();
        }
        System.out.println(this.queue);
        return this.queue.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
// @lc code=end

