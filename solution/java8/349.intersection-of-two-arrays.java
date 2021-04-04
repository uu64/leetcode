/*
 * @lc app=leetcode id=349 lang=java
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
import java.util.*;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int idx1 = 0;
        int idx2 = 0;
        Set<Integer> intersection = new HashSet<>();
        while (idx1 < nums1.length && idx2 < nums2.length) {
            int v1 = nums1[idx1];
            int v2 = nums2[idx2];
            if (v1 == v2) {
                intersection.add(v1);
                idx1 += 1;
                idx2 += 1;
            } else if (v1 < v2) {
                idx1 += 1;
            } else if (v2 < v1) {
                idx2 += 1;
            }
        }

        int[] ans = new int[intersection.size()];
        int idx = 0;
        for (int v: intersection) {
            ans[idx] = v;
            idx++;
        }

        return ans;
    }
}
// @lc code=end

