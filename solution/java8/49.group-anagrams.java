/*
 * @lc app=leetcode id=49 lang=java
 *
 * [49] Group Anagrams
 */

// @lc code=start

import java.util.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int N = strs.length;
        List<Map<String, Integer>> counters = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            Map<String, Integer> counter = new HashMap<>();
            for (String s: strs[i].split("")) {
                if (counter.containsKey(s)) {
                    int tmp = counter.get(s);
                    counter.put(s, tmp + 1);
                } else {
                    counter.put(s, 1);
                }
            }
            counters.add(counter);
        }

        List<List<String>> ans = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (strs[i] == null) {
                continue;
            }
            List<String> words = new ArrayList<>();
            words.add(strs[i]);
            for (int j = i+1; j < N; j++) {
                if (counters.get(i).equals(counters.get(j))) {
                    words.add(strs[j]);
                    strs[j] = null;
                }
            }
            ans.add(words);
        }

        return ans;
    }
}
// @lc code=end

