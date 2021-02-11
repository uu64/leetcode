#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                if stack.pop() != brackets[c]:
                    return False

        if len(stack) != 0:
            return False

        return True


# @lc code=end

