class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                count = 0
                directions = [
                    (-1, -1),
                    (0, 1),
                    (1, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                    (1, -1),
                    (-1, 1),
                ]

                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                        count += 1

                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = -1

                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == -1:
                    board[i][j] = 0
