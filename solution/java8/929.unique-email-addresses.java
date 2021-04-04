/*
 * @lc app=leetcode id=929 lang=java
 *
 * [929] Unique Email Addresses
 */

// @lc code=start
import java.util.*;

class Solution {
    public int numUniqueEmails(String[] emails) {
        Map<String, Set<String>> mailMap = new HashMap<>();
        for (String mail: emails) {
            String[] parts = mail.split("@");
            String local = parts[0];
            String domain = parts[1];

            StringBuilder sb = new StringBuilder();
            for (char c: local.toCharArray()) {
                if (c == '+') {
                    break;
                }
                if (c == '.') {
                    continue;
                }
                sb.append(c);
            }
            String key = sb.toString();
            if (!mailMap.containsKey(key)) {
                mailMap.put(key, new HashSet<String>());
            }
            mailMap.get(key).add(domain);
        }

        int ans = 0;
        for (Map.Entry<String, Set<String>> entry: mailMap.entrySet()) {
            ans += entry.getValue().size();
        }
        return ans;
    }
}
// @lc code=end

