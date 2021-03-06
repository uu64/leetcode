#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [ [ 0 for i in range(n) ] for j in range(m) ]

        paths[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i > 0 and obstacleGrid[i-1][j] == 0:
                    paths[i][j] += paths[i-1][j]
                if j > 0 and obstacleGrid[i][j-1] == 0:
                    paths[i][j] += paths[i][j-1]
        return paths[-1][-1]


# @lc code=end

