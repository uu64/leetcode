/*
 * @lc app=leetcode id=283 lang=java
 *
 * [283] Move Zeroes
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        int N = nums.length;
        int pos = 0;
        for (int i = 0; i < N; i++) {
            if (nums[i] != 0) {
                nums[pos] = nums[i];
                pos++;
            }
        }
        for (int i = pos; i < N; i++) {
            nums[i] = 0;
        }
    }
}
// @lc code=end

