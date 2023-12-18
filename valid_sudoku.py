from typing import List


def isValid(x):
    print(x)
    nums = [q for q in x if q != '.']
    return len(list(set(nums))) == len(nums)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                if not isValid(board[i * 3 + j]):
                    return False
                if not isValid([x[i * 3 + j] for x in board]):
                    return False

                cell_rows = [board[k] for k in range(i* 3, i*3 + 3)]
                cell = [row[k] for row in cell_rows for k in range(j*3, j*3+3)]
                if not isValid(cell):
                    return False

        return True

        