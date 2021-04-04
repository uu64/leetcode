/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int i: nums) {
            if (counter.containsKey(i)) {
                int val = counter.get(i);
                counter.put(i, val + 1);
            } else {
                counter.put(i, 1);
            }
        }

        PriorityQueue<Map.Entry<Integer, Integer>> queue
            = new PriorityQueue<>(Map.Entry.comparingByValue(Comparator.reverseOrder()));
        for (Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            queue.add(entry);
        }

        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            Map.Entry<Integer, Integer> entry = queue.poll();
            ans[i] = entry.getKey();
        }
        return ans;
    }
}
// @lc code=end

