class Solution:
    def __init__(self):
        self.result_dict = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if 0 < n < 3:
            return 1

        if n not in self.result_dict:
            self.result_dict[n] = self.tribonacci(
                n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.result_dict[n]


s = Solution()
print(s.tribonacci(n=25), 1389537)
