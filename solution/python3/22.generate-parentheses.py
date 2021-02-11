#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []

        def main(s):
            if len(s) == 2*n:
                answer.append(s)
                return

            if s.count('(') < n:
                main(s + '(')
            if s.count(')') < s.count('('):
                main(s + ')')

        main('')
        return answer

# @lc code=end

