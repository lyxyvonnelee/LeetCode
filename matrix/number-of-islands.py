class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= m or c >= n or r < 0 or c < 0 or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r, c-1)
            dfs(r, c+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count