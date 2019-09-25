# coding:utf-8
M = 4


def check(board, row, col):
    i = 0
    while i < row:
        if abs(col - board[i]) in (0, abs(row - i)):
            return False
        i += 1
    return True


# 递归实现
def EightQueen(board, row):
    blen = len(board)
    if row == blen:  # 来到不存在的第九行了
        print(board)
        printBoard(board)
        return True  # 一定要return一个True，理由在下面
    col = 0
    while col < blen:
        if check(board, row, col):
            board[row] = col
            if EightQueen(board, row + 1):
                pass
                # return True #此处为找出一个解就结束
        col += 1
    return False


def printBoard(board):
    '''为了更友好地展示结果 方便观察'''
    import sys
    for i, col in enumerate(board):
        sys.stdout.write('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
        print('')


if __name__ == '__main__':
    board = [0] * M
    row = 0
    EightQueen(board, row)
