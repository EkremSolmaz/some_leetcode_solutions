from typing import List


class Solution:
    def is_neighbor(self, board: List[List[str]], i, j, char: str):
        n, m = len(board), len(board[0])
        cut = board[max(i-1, 0):min(i+1, n-1)][max(j-1, 0):min(j+1, m-1)]
        any([0 in x for x in a])

    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        i, j = 0, 0

        while i < n and j < m:
            any([0 in x for x in a])

        pass


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
      ["A", "D", "E", "E"]], "ABCCED"))
