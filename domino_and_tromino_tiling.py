# fuck this question
class Solution:
    def __init__(self):
        self.results = {}

    def numTilings(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 2
        if n == 3:
            return 5

        if n not in self.results:
            self.results[n] = (self.numTilings(n-1) * 2 +
                               self.numTilings(n-3)) % (10**9 + 7)
        return self.results[n]
