class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtrack(n, 0, chessboard, result)
        return result
    
    def backtrack(self, n, row, board, res):
        if row == n:
            res.append(board[:])
            return

        for col in range(n):
            if self.isValid(row, col, board): 
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.backtrack(n, row+1, board, res)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def isValid(self, row, col, board):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i, j, n = row-1, col+1, len(board)
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True       