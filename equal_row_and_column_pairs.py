from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d_row = {}
        d_col = {}
        res = 0

        for i in range(n):
            row_str = "-".join([str(x) for x in grid[i]])
            col_str = "-".join([str(a[i]) for a in grid])
            d_row[row_str] = d_row.get(row_str, 0) + 1
            d_col[col_str] = d_col.get(col_str, 0) + 1

        for k, v in d_row.items():
            res += d_col.get(k, 0) * v

        return res


print("Expected: 1, Result:", Solution().equalPairs(
    grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print("Expected: 3, Result:", Solution().equalPairs(
    grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
