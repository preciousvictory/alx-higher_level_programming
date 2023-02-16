#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard. Write a
program that solves the N queens problem.

- Usage: nqueens N
    If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
 
- where N must be an integer greater or equal to 4
    - If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    - If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1

- Format: [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys
class Solution:
    def __init__(self, size=0):
        self.row = size
        self.col = size

    def board_(self):
        """Initialize NxN chessboard"""
        board = []
        for cor in range(self.row):
            c=[]
            [c.append('#') for i in range(self.col)]
            board.append(c)

        c = 0
        for r in range(self.row): 
            board[r][c] = '-'
            c += 1

        for i in board: print(i)
        return board

    def del_invalid(self, board, row, col):
        """If Queen positon is determine, this method give the value '-' to every other positon that
        share the same row, column, or diagonal. 

        Args:
            row: row postion of queen
            col: column position of queen

        Returns:
            board
        """
        l = len(board)

        """Forward after Q"""
        for r in range(col + 1, l):
            board[row][r] = '-'
        
        """Backward before Q"""
        for r in range(col - 1, -1, -1):
            board[row][r] = '-'
        
        """Downward after Q"""
        for r in range(row + 1, l):
            board[r][col] = '-'

        """Upward before Q"""
        for r in range(row - 1, -1, -1):
            board[r][col] = '-'

        """Diagonally downwards right"""
        c = col + 1 
        for r in range(row + 1, l):
            if c >= len(board):
                break
            board[r][c] = '-'
            c += 1

        """Diagonally downwards left"""
        c = col - 1
        for r in range(row + 1, l):
            if c < 0:
                break
            board[r][c] = '-'
            c -= 1

        """Diagonally upwards left"""
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            board[r][c] = '-'
            c -= 1

        """Diagonally upwards right"""
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c  >= len(board):
                break
            board[r][c] = '-'
            c += 1
        return board
    
    def valid_queen(self, board, l):
        """if postion is valid it give the value 'Q' to that positon

        Args:
            board: NxN board

        Returns: 
            board
        """
        r = 0
        position = []
        for rol in board:
            c = 1 
            pos = []
            for col in rol:
                if board[r][c] != '-' and board[r][c] != 'Q':
                    board[r][c] = 'Q'
                    pos.append(r)
                    pos.append(c)
                    board = self.del_invalid(board, r, c)
                    if c >= len(board):
                        break
                c += 1
            position.append(pos)
            r += 1
            
        print(r,c)
        return board, position
        

if __name__ == "__main__":
    length = len(sys.argv)
    if length != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])

    if type(N) is not int:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    sol = Solution(N)

    board = sol.board_()
    board, position = sol.valid_queen(board, 1)
    for i in board: print(i)

    print(position)
