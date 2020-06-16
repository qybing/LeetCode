#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/6/15 18:57 
# @Author : Jovan
# @File : is_valid_sudoku.py
# @desc :
def isValidSudoku(board):
    row = [set([]) for i in range(9)]
    col = [set([]) for i in range(9)]
    grid = [set([]) for i in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            if board[i][j] in row[i]:
                return False
            if board[i][j] in col[j]:
                return False
            g = int(i / 3 * 3 + j / 3)

            if board[i][j] in grid[g]:
                return False
            grid[g].add(board[i][j])
            row[i].add(board[i][j])
            col[j].add(board[i][j])
    return True
a = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(a))
