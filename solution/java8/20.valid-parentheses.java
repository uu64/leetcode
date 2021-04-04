/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<String>();
        String[] chars = s.split("");
        Map<String, String> parentheses = new HashMap<>();
        parentheses.put("(", ")");
        parentheses.put("{", "}");
        parentheses.put("[", "]");

        for (String c: chars) {
            if (parentheses.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                String opener = stack.pop();
                if (c.equals(parentheses.get(opener))) {
                    continue;
                } else {
                    return false;
                }
            }
        }

        return stack.isEmpty();

    }
}
// @lc code=end

