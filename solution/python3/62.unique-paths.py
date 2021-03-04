#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [ [ 0 for j in range(n) ] for i in range(m) ]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    paths[i][j] += paths[i-1][j]
                if j > 0:
                    paths[i][j] += paths[i][j-1]

        return paths[-1][-1]
# @lc code=end

