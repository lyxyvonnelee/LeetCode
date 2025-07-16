class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != "O":
                return

            board[row][col] = "S"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)

        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
