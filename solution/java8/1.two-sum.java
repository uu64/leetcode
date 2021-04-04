/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int N = nums.length;
        int[] ans = new int[2];
        boolean finish = false;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (nums[i] + nums[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                    finish = true;
                    break;
                }
            }
            if (finish) {
                break;
            }
        }
        return ans;
    }
}
// @lc code=end

