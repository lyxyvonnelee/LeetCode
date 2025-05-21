class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        effort_to = [[float('inf')] * n for _ in range(m)]
        effort_to[0][0] = 0
        efforts = [(0, 0, 0)]

        while efforts:
            effort, x, y = heapq.heappop(efforts)

            if x == m-1 and y == n-1:
                return effort

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                    current_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if current_effort < effort_to[nx][ny]:
                        effort_to[nx][ny] = current_effort
                        heapq.heappush(efforts, (current_effort, nx, ny))
        
        return 0
