class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*n

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]
        
        return dp[-1]

