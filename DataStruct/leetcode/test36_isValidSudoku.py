class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxs = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    box_index = int((i // 3) * 3 + j // 3)
                    boxs[box_index][num] = boxs[box_index].get(num, 0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxs[box_index][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    nums = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution()
    print(s.isValidSudoku(nums))
