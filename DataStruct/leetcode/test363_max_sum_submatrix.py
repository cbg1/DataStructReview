# coding:utf-8
def max_sum_submatrix(matrix, k):
    rows, columns = len(matrix), len(matrix[0])
    print(rows, columns)


if __name__ == '__main__':
    matrix = [[1, 0, 1], [0, -2, 3]]
    max_sum_submatrix(matrix, 2)
