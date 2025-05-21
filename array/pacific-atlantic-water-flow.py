class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
              return []
         
        m, n = len(heights), len(heights[0])

        pacific_reachable = [[False]*n for _ in range(m)]
        atlantic_reachable = [[False]*n for _ in range(m)]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j, reachable):
            reachable[i][j] = True
            for dx, dy in directions:
                nx, ny = i+dx, j+dy
                if 0 <= nx < m and 0 <= ny < n and not reachable[nx][ny] and heights[nx][ny] >= heights[i][j]:
                    dfs(nx, ny, reachable)

        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n-1, atlantic_reachable)

        for j in range(n):
            dfs(0, j, pacific_reachable)
            dfs(m-1, j, atlantic_reachable)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i,j])

        return result
         
